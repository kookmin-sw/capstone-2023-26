from django.db import models

# Create your models here.

class Event(models.Model):
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    event_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    coordinate = models.JSONField()
    crowd = models.JSONField()
    is_being_held = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['id']