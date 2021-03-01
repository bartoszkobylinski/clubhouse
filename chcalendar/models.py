from django.db import models

# Create your models here.

class CHRoom(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    description = models.TextField()
    
class Host(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.URLField()
    room = models.ForeignKey(CHRoom, on_delete=models.CASCADE)
    