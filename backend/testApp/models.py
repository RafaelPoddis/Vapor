from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    price = models.FloatField()
    description = models.TextField()
    isAdults = models.BooleanField()
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    about = models.TextField(blank=True)
    level = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} - Level: {self.level}"

class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField()
    body = models.TextField()
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"Made by {self.user} - Rate: {self.value}"

class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=15)

    def __str__(self):
        return self.name

class GameGenre(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="game_genre")
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, related_name="genre_game")

    def __str__(self):
        return f"{self.game.name} - {self.genre.name}"

class UserGame(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="game_users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_games")
    achievements = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} has {self.achievements} achievements for {self.game.name}"
    
