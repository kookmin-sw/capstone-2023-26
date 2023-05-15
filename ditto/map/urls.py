from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import test

# router = routers.DefaultRouter()
# router.register("HeadCount", views.HeadCountViewSet)

urlpatterns  = [
    path('', test )
]