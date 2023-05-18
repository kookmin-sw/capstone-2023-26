from django.db import models

# Create your models here.

class DroneInfo(models.Model):
    time = models.DateTimeField()
    coordinate = models.JSONField()
    voltage = models.FloatField()
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']
    
class HeadCount(models.Model):
    row = models.IntegerField(null=False, blank=False)
    col = models.IntegerField(null=False, blank=False)
    coordinate = models.JSONField(null=False, default=[0.0, 0.0])
    update_time = models.DateTimeField(auto_now=True)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    count = models.IntegerField(null=False, default=0)

    class Meta:
        ordering = ['id']

class CountHistory(models.Model):
    update_time = models.DateTimeField(auto_now=True)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    count = models.IntegerField(null=False, default=0)

    class Meta:
        ordering = ['id']