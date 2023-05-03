from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'user_id', 'city', 'event_name', 'location', 'coordinate', 'crowd', 'is_being_held')