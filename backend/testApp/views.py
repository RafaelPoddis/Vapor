from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .forms import GamesForm
from .models import Games
from .serializer import GameSerializer

# Create your views here.
class GameDetail(APIView):
    def get(self, request, gameName):
        try:
            game = Games.objects.get(name=gameName)
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Games.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

class GameView(APIView):
    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        games = Games.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, gameName):
        try:
            game = Games.objects.get(name=gameName)
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Games.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, gameName, format=None):
        try:
            jogo = Games.objects.get(name=gameName)
            jogo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Games.DoesNotExist:
            return Response({"error": "Jogo não encontrado"}, status=status.HTTP_404_NOT_FOUND)

# class RatingsView(APIView):
#     def post(self, request):

def index(request):
    return render(request, "index.html")