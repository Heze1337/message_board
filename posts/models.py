from django.utils import timezone
from django.db import models
from django.contrib import admin

class Post(models.Model):
    text = models.TextField()
    data = models.DateField(default=timezone.now)
    temperature = models.FloatField(default=0.0)
    pressure = models.IntegerField(default=0)
    wind_speed = models.FloatField(default=0)
    precipitation_probability = models.IntegerField(default=0)
    

class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "data", "temperature", "pressure", "wind_speed", "precipitation_probability"]