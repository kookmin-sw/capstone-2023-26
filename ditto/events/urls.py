from django.contrib import admin
from django.urls import path, include
from .views import admin_events, user_events, map, control, control_detail, area

urlpatterns = [
    path('administer/', admin_events),
    path('user/<int:city_id>', user_events, name="user"),
    path('user/map/<int:event_id>', map, name="map"),
    path('control/<int:event_id>/', control, name="control"),
    path('control/detail/', control_detail, name="control_detail"),
    path('', area, name='area')
]