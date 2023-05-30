from django.db import models
# Create your models here.

class Event(models.Model):
    keyword = models.CharField(max_length=30)
    distance = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    # objects = models.manager()
    def __str__(self):
        return self.category
