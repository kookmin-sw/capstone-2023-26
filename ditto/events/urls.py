from django.contrib import admin
from django.urls import path, include
from .views import admin_events, user_events, control, control_detail

urlpatterns = [
    path('admin/', admin_events),
    path('user/', user_events),
    path('control/<int:event_id>/', control, name="control"),
    path('control/detail/', control_detail, name="control_detail"),
]