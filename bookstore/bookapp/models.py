from django.db import models

# Create your models here.
class Request(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    date = models.DateField()
    comment = models.CharField(max_length = 1000)
