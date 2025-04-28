from django.db import models
from datetime import timedelta
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
    name = models.CharField(unique=True, max_length=50)
    price = models.FloatField()
    description = models.TextField()
    isAdults = models.BooleanField()
    genres = models.ManyToManyField(Genres, related_name="genres")
    achievements = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

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
    time_played = models.DurationField(default=timedelta(0))
    session_start = models.DateTimeField(blank=True, null=True)

    def start_gaming_session(self):
        """Marca o início de uma sessão de jogo"""
        self.session_start = now()
        self.last_played = self.session_start
        self.save()

    def end_gaming_session(self):
        """Finaliza a sessão de jogo e atualiza o tempo total"""
        if self.session_start:
            # Calcula o tempo da sessão atual
            session_duration = now() - self.session_start
            # Adiciona ao tempo total
            self.time_played += session_duration
            # Atualiza last_played e limpa session_start
            self.last_played = now()
            self.session_start = None
            self.save()
            return session_duration
        return None

    def __str__(self):
        return f"{self.user.username} has {self.achievements} achievements for {self.game.name}\nLast Played: {self.last_played}"
    
