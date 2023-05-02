from django.db import models

# Create your models here.

class Location(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    location = models.JSONField()
    crowd = models.JSONField()
    is_being_held = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['id']