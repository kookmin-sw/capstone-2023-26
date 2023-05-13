from rest_framework import serializers
from .models import HeadCount

class HeadCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCount
        fields = ("__all__")
