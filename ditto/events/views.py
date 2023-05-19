from django.shortcuts import render, redirect

# Create your views here.

from rest_framework import viewsets
from .serializers import EventSerializer, CitySerializer, AlertLogSerializer, RecordingLogSerializer
from .models import Event, City, AlertLog, RecordingLog
from map.models import HeadCount, DroneInfo

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class AlertLogViewSet(viewsets.ModelViewSet):
    queryset = AlertLog.objects.all()
    serializer_class = AlertLogSerializer
    
class RecordingLogViewSet(viewsets.ModelViewSet):
    queryset = RecordingLog.objects.all()
    serializer_class = RecordingLogSerializer
    
def admin_events(request):
    name = 'admin'
    events = Event.objects.filter(user_id=request.user.id) # 진행 여부와 상관없이 자신이 관리하는 모든 행사
    
    #return render(request, "../templates/location_admin.html", {"events": events})
    return redirect('control', 1)

def user_events(request, city_id):
    name = 'user'
    events = Event.objects.filter(is_being_held=1, city_id=city_id) # 진행중인 모든 행사
    
    return render(request, "../templates/location_user.html", {"events": events})

def control(request, event_id):
    name = 'control'
    events = Event.objects.filter(user_id=request.user.id)
    event = Event.objects.get(id=event_id)
    
    headcount = HeadCount.objects.filter(id=event_id)
    droneinfo = DroneInfo.objects.filter(id=event_id).last()
    return render(request, '../templates/control.html', {'event': event, 'events':events, 'event_id':event_id, 'headcounts': headcount, 'droneinfo': droneinfo})

def map(request, event_id):
    name = 'map'
    coordinate = Event.objects.get(id=event_id).coordinate
    
    headcount = HeadCount.objects.filter(event_id_id=event_id)
    return render(request, "../templates/map.html", {'coordinate': coordinate, 'headcounts': headcount})

def control_detail(request):
    name = 'control_detail'
    return render(request, '../templates/control_detail.html')

def control_record(request, event_id):
    name = 'control_record'
    
    record = RecordingLog.objects.get(event_id=event_id)
    return render(request, '../templates/control_record.html', {'records': record})

def area(request):
    name = 'area'
    
    city_list = City.objects.all()
    return render(request, '../templates/area.html', {'city_list': city_list})

def initHeadcount(request, event_id):
    HeadCount.objects.all().delete()
    return redirect('control', event_id)