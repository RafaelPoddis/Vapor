from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

def game_media_path(instance, filename):
    return f"games/{instance.game.id}/media/{filename}"
# Create your models here.
class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=15)

    def __str__(self):
        return self.name

class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    price = models.FloatField()
    description = models.TextField()
    isAdults = models.BooleanField()
    genres = models.ManyToManyField(Genres, related_name="genres")

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    about = models.TextField(blank=True)
    level = models.IntegerField(default=0)

    def update_last_login(self):
        self.last_login = now()
        self.save()

    def __str__(self):
        return f"{self.username} - Level: {self.level}"
    
class GameMedia(models.Model):
    GAME_MEDIA_TYPES = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="media")
    media_type = models.CharField(max_length=10, choices=GAME_MEDIA_TYPES)
    file = models.FileField(upload_to=game_media_path)

class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField()
    body = models.TextField()
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"Made by {self.user} - Rate: {self.value}"


class UserGame(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="game_users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_games")
    achievements = models.IntegerField(default=0)
    last_played = models.DateTimeField(blank=True, null=True)

    def update_last_played(self):
        self.last_played = now()
        self.save()

    def __str__(self):
        return f"{self.user.username} has {self.achievements} achievements for {self.game.name}\nLast Played: {self.last_played}"
    
