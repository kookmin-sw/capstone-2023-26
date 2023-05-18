from django.contrib import admin
from .models import Event, City, RecordingLog

# Register your models here.    

admin.site.register(Event)
admin.site.register(City)
admin.site.register(RecordingLog)