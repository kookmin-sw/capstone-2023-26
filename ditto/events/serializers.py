from rest_framework import serializers
from .models import Event, City, AlertLog, RecordingLog

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("__all__")
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("__all__")
        
class AlertLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlertLog
        fields = ("__all__")
        
class RecordingLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecordingLog
        fields = ("__all__")