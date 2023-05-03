from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
def control(request):
    name = 'control'
    events = Event.objects.filter(user_id=request.user.id)
    
    return render(request, "../templates/location_list.html", {"events": events})

def user(request):
    
    name = 'main'
    events = Event.objects.all()
    
    return render(request, "../templates/location_list.html", {"events": events})