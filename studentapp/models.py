from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    marks = models.FloatField()
    phone = models.BigIntegerField()
