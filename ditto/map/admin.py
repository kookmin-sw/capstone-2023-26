from django.contrib import admin
from .models import DroneInfo, HeadCount, CountHistory

# Register your models here.

admin.site.register(DroneInfo)
admin.site.register(HeadCount)
admin.site.register(CountHistory)