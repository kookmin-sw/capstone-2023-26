from typing import Any
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import HeadCountSerializer, DroneInfoSerializer
from .models import HeadCount, DroneInfo, CountHistory
from events.models import Event
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import math
from datetime import datetime, timedelta
from time import time
from django.db.models import Sum


# Create your views here.
class DroneInfoViewSet(viewsets.ModelViewSet):
    queryset = DroneInfo.objects.all()
    serializer_class = DroneInfoSerializer

class HeadCountAPI(APIView):

    # def __init__(self):
    #     super().__init__()
    #     print("__init__")
    #     self.record = DroneInfo.objects.order_by("time").first()
    #     print("event_id!!!!: ", self.record.event_id)
    #     print("event_id!!!!: ", self.record.time)
    #     print("event_id!!!!: ", self.record.coordinate)
    #     print("event_id!!!!: ", self.record.voltage)

    def get(self, request):

        queryset = HeadCount.objects.all()
        serializer = HeadCountSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):

        js = json.loads(request.body)
        print(js)
        count = js["count"]
        time = js["timestamp"]
        print(time, count)

        inputdt = datetime(year=int(time[:4]), month=int(time[5:7]), day=int(time[8:10]), hour=int(time[11:13]), minute=int(time[14:16]), second=int(time[17:19]))
        # to_dt = datetime(year=int(t_to[:4]), month=int(t_to[4:6]), day=int(t_to[6:8]), hour=int(t_to[8:10]), minute=int(t_to[10:12]), second=int(t_to[12:14]))
        
        #now_t = datetime.time(inputdt)
        #from_t = datetime.time(inputdt - timedelta(minutes=3))
        #end_t = datetime.time(inputdt + timedelta(minutes=3))
        
        #now_t = now_t.strftime('%H:%M:%S')
        #now_t = f'{now_t:%HH:%MM:%ss}'
        '''
        from_t = f'{from_t:%H:%M:%S}'
        end_t = f'{end_t:%H:%M:%S}'
        '''
        drone_records = DroneInfo.objects.filter(time__lte=time).order_by("-time").first()
        print(drone_records)
        # FK로 해당 event object 다 가져와짐 
        event = drone_records.event_id

        # 중심 위도 경도
        c_lat = event.coordinate[0]
        c_lng = event.coordinate[1]
        
        # print(drone_records.time, drone_records.coordinate, drone_records.event_id)
        
        # 새로운 위도 경도
        new_lat = drone_records.coordinate[0]
        new_lng = drone_records.coordinate[1]

        # 반경 몇미터를 볼 것인지 지정
        m = event.range

        # 총 그리드를 몇바이 몇으로 할것인지 지정 
        divide_by = event.num_div

        # 중심 x,y 인덱스 계산 
        cx = divide_by / 2
        cy = divide_by / 2
        # 한 인덱스당 실제로 몇 미터를 커버하는지 산정 
        per_idx = m / divide_by 

        x, y = Plot.find_index(cx, cy, c_lat, c_lng, new_lat, new_lng, per_idx)
        print(x, y)
        
        exist = HeadCount.objects.filter(row=y, col=x)
        if len(exist):
            print("modify")
            exist[0].count = count
            exist[0].save()
        else: 
            print("create new")
            new = HeadCount(row=y, col=x, count=count)
            event_id = drone_records.event_id
            new.event_id = event_id
            new.save()
        
        serializer = HeadCountSerializer(data=request.data)
        if serializer.is_valid():
            print("is_valid()")
            
            return Response(serializer.data)
          
        return Response(serializer.errors)

class Plot:
    def __init__(self):
        pass

    def calculate_distance(lat1, lon1, lat2, lon2):
        # Earth's radius in meters
        earth_radius = 6371000

        # Convert latitudes and longitudes to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Calculate the differences in radians
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        # Calculate the differences in kilometers
        distance_lat = delta_lat * earth_radius
        distance_lon = delta_lon * earth_radius * math.cos((lat1_rad + lat2_rad) / 2)

        return round(distance_lat, 6), round(distance_lon, 6)
    
    def find_index(cx, cy, clat, clng, new_lat, new_lng, per_idx):
        # calculate_distance를 통해 중앙점에서 새로운 드론 지점까지 몇미터가 차이나는지 계산
        # 위도기준 몇미터 차이나는지 경도기준 몇미터 차이나는지 반환
        diff_lat, diff_lng = Plot.calculate_distance(clat, clng, new_lat, new_lng)
        print(f"미터 차이: {diff_lat}, {diff_lng}")
        
        # 단위 면적으로 나눠줌 - 몇 인덱스 움직이는지 파악하기 위함
        diff_lat /= per_idx 
        diff_lng /= per_idx
        
        # 중심 좌표로부터 이동
        cx += diff_lat
        cy += diff_lng
        
        # flooring 하여 반환
        return int(cx), int(cy)
    
