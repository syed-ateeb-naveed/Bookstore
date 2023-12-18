from django.db import models
from datetime import datetime, date
from django.utils import timezone

# Create your models here.
class Request(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    date = models.DateField(default = date.today())
    comment = models.CharField(max_length = 1000)
