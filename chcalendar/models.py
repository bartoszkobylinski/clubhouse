from django.db import models

# Create your models here.

class CHRoom(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.date}"
    
    
class Host(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.URLField()
    room = models.ForeignKey(CHRoom, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    