from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Games(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    price = models.FloatField()
    description = models.TextField()
    isAdults = models.BooleanField()
    # genres = ArrayField(models.CharField(max_length=20), size=5)
