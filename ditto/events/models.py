from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['id']
class Event(models.Model):
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    city = models.ForeignKey("events.City", on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    coordinate = models.JSONField()
    crowd = models.JSONField()
    is_being_held = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['id']