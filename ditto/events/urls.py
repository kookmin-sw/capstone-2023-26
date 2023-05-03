from django.contrib import admin
from django.urls import path, include
from .views import control, user

urlpatterns = [
    path('admin', control),
    path('user', user)
]