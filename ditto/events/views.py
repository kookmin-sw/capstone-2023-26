from django.shortcuts import render, redirect
import boto3
import subprocess
from urllib import parse
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

from rest_framework import viewsets
from .serializers import EventSerializer, CitySerializer, AlertLogSerializer, RecordingLogSerializer
from .models import Event, City, AlertLog, RecordingLog
from map.models import HeadCount, DroneInfo, CountHistory

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
    history = CountHistory.objects.filter(event_id_id=event_id).order_by('update_time')
    # times = history.values('update_time')
    length = len(history)
    print(length)
    if length > 10:
        history = history[length-10:]
        # times = times[length-10:]
    tmp_times = []
    # for time in times:
    #     tmp_times.append(time['update_time'].strftime('%Y-%m-%d %H:%M:%S'))
        # print(time)
    headcount = HeadCount.objects.filter(event_id_id=event_id)
    droneinfo = DroneInfo.objects.filter(event_id=event_id).last()

    return render(request, '../templates/control.html', {'event': event, 'events':events, 'event_id':event_id, 'headcounts': headcount, 'droneinfo': droneinfo, 'historys': history, 'times': tmp_times})


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
    
    record = RecordingLog.objects.filter(event_id=event_id)
    return render(request, '../templates/record.html', {'records': record})

def control_play(request):
    name = 'control_play'

    return render(request, '../templates/play.html')

def area(request):
    name = 'area'
    
    city_list = City.objects.all()
    return render(request, '../templates/area.html', {'city_list': city_list})

def eventAdd(request, event_id):
    name = 'event-add'
    return render(request, '../templates/event-add.html', {'event_id': event_id})

def createEvent(request, event_id):
    name = 'createEvent'
    # print(request.POST.get("name"), request.POST.get("location"), request.POST.get("coordinate"), request.POST.get("isheld"))
    if request.method == "POST":
        event_name = request.POST.get("event_name", False)
        location = request.POST.get("location", False)
        coordinate = request.POST.get("coordinate", False)
        isheld = request.POST.get("isheld", False)
        if isheld == "on":
            isheld = True
        else:
            isheld = False
        
        tmp = Event.objects.get(id=event_id)
        city = tmp.city

        event = Event(event_name=event_name, location=location, coordinate=coordinate, is_being_held=isheld, user_id_id=request.user.id, city_id=city.id)
        event.save()

    return redirect('control', event_id)


def initHeadcount(request, event_id):

    HeadCount.objects.filter(event_id=event_id).delete()
    return redirect('control', event_id)


def download_video(request, key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    response = s3_client.get_object(
        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        Key=parse.unquote(key)
    )
    
    content_type = response['ContentType']
    response_data = response['Body'].read()
    
    response = HttpResponse(response_data, content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename={}'.format(key)
    print(type(response))
    return response
