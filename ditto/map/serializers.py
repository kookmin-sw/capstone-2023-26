from rest_framework import serializers
from .models import HeadCount, DroneInfo

class HeadCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCount
        fields = ("__all__")
        
class DroneInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DroneInfo
        fields = ("__all__")
