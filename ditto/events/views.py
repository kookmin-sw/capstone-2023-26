from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import EventSerializer, CitySerializer
from .models import Event, City

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
def admin_events(request):
    name = 'admin'
    events = Event.objects.filter(user_id=request.user.id) # 진행 여부와 상관없이 자신이 관리하는 모든 행사
    
    return render(request, "../templates/location_admin.html", {"events": events})

def user_events(request, city_id):
    name = 'user'
    events = Event.objects.filter(is_being_held=1, city_id=city_id) # 진행중인 모든 행사
    
    return render(request, "../templates/location_user.html", {"events": events})

def map(request, event_id):
    name = 'map'
    coordinate = Event.objects.get(id=event_id).coordinate
    return render(request, "../templates/map.html", {'coordinate': coordinate})

def control(request, event_id):
    name = 'control'
    coordinate = Event.objects.get(id=event_id).coordinate
    return render(request, '../templates/control.html', {'coordinate': coordinate})

def control_detail(request):
    name = 'control_detail'
    return render(request, '../templates/control_detail.html')

def area(request):
    name = 'area'
    
    city_list = City.objects.all()
    return render(request, '../templates/area.html', {'city_list': city_list})