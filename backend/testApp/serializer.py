from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()  # Puxa os dados das avaliações manualmente
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Games
        fields = '__all__'

    def get_ratings(self, obj):
        return [
            {"id": r.id, "value": r.value, "body": r.body, "user": r.user.id}
            for r in obj.ratings.all()
        ]
    
    def get_genres(self, obj):
        return [
            {"id": g.id, "name": g.name}
            for g in obj.genres.all()
        ]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    user_games = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_ratings(self, obj):
        return [
            {"id": r.id, "value": r.value, "body": r.body, "game": r.game.id}
            for r in obj.ratings.all()
        ]
    
    def get_user_games(self, obj):
        return [
            {"id": g.game.id, "name": g.game.name, "achievements": g.achievements}
            for g in obj.user_games.all()
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'