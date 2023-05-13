from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeadCountSerializer
from .models import HeadCount
from django.http import HttpResponse, JsonResponse


# Create your views here.
class HeadCountViewSet(viewsets.ModelViewSet):
    queryset = HeadCount.objects.all()
    serializer_class = HeadCountSerializer

def test(self, request):
    dummy_data = {
        'name': '죠르디',
        'type': '공룡',
        'job': '편의점알바생',
        'age': 5
    }
    return JsonResponse(dummy_data)