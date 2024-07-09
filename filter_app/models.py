from django.db import models

# Create your models here.

from django.db import models

class JobDescription(models.Model):
    content = models.TextField()
    status = models.CharField(max_length=10, default='Pending')

class ProhibitedPattern(models.Model):
    pattern = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
