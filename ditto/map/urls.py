from django.contrib import admin
from django.urls import path, include
from .views import test

# router = routers.DefaultRouter()
# router.register("HeadCount", views.HeadCountViewSet)

urlpatterns  = [
    path('',  test)
]