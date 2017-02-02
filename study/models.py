from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=10)
    text = models.TextField()
    
    def __str__(self):
        return self.level