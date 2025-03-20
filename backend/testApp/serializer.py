from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'