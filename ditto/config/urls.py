"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events.views import EventViewSet, CityViewSet, AlertLogViewSet, RecordingLogViewSet
from .views import home, clientmap
from events import views
from map import views
from map.views import HeadCountViewSet, DroneInfoViewSet


router = routers.DefaultRouter()
router.register('event', EventViewSet)
router.register('city', CityViewSet)
router.register('headcount', HeadCountViewSet)
router.register('alertlog', AlertLogViewSet)
router.register('recordinglog', RecordingLogViewSet)
router.register('droneinfo', DroneInfoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('events.urls')),
    path('clientmap/', clientmap),
    path('test/', home),

]
