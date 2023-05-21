from django.contrib import admin
from django.urls import path, include
from .views import admin_events, user_events, map, control, control_detail, area, control_record, initHeadcount, download_video, eventAdd, createEvent

urlpatterns = [
    path('administer/', admin_events),
    path('<int:city_id>', user_events, name="user"),
    path('<int:event_id>/map', map, name="map"),
    path('administer/<int:event_id>/', control, name="control"),
    path('administer/add/<int:event_id>', eventAdd, name="event-add"),
    path('control/detail/', control_detail, name="control_detail"),
    path('administer/<int:event_id>/record', control_record, name="record"),
    path('control/init/<int:event_id>', initHeadcount, name="initHeadcount"),
    path('control/record/download/<str:key>', download_video, name='download_video'),
    path('', area, name='area'),
    path('createEvent/<int:event_id>', createEvent, name='createEvent')
]