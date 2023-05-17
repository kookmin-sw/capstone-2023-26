from django.contrib import admin
from django.urls import path, include
from .views import admin_events, user_events, map, control, control_detail, area, control_record

urlpatterns = [
    path('administer/', admin_events),
    path('<int:city_id>', user_events, name="user"),
    path('<int:event_id>/map', map, name="map"),
    path('administer/<int:event_id>/', control, name="control"),
    path('control/detail/', control_detail, name="control_detail"),
    path('control/record/', control_record, name="record"),
    path('', area, name='area')
]