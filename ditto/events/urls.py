from django.contrib import admin
from django.urls import path, include
from .views import admin_events, user_events, control

urlpatterns = [
    path('admin/', admin_events),
    path('user/', user_events),
    path('control/<int:event_id>/', control, name="control"),
]