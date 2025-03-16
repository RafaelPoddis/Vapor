from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Games(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    price = models.FloatField()
    description = models.TextField()
    isAdults = models.BooleanField()

    def __str__(self):
        return f"{self.name}\n{self.price}\n{self.description}\n{self.isAdults}"

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="avatars/")
    about = models.TextField()
    level = models.IntegerField()

class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField()
    body = models.TextField()
    game_name = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="ratings")

