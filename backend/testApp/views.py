from .serializer import *
from .models import Games
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

# Create your views here.
class GameDetail(APIView):
    def get(self, request, game_id):
        try:
            game = Games.objects.get(id=game_id)
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
    
    def put(self, request, game_id):
        try:
            game = Games.objects.get(id=game_id)
            serializer = GameSerializer(game, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Games.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, game_id, format=None):
        try:
            jogo = Games.objects.get(id=game_id)
            jogo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Games.DoesNotExist:
            return Response({"error": "Game Not Found"}, status=status.HTTP_404_NOT_FOUND)

class RatingsView(APIView):
    # def post(self, request, game_id):
    #     try:
    #         game = Games.objects.get(id=game_id)
    #     except Games.DoesNotExist:
    #         return Response({"error: Game Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
    #     request.data["game"] = game.id
    #     serializer = RatingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, game_id):
        game = get_object_or_404(Games, id=game_id)
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.data["game"] = game.id
        request.data["user"] = user.id  

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            game.rating_count += 1
            game.save()

            user.rating_count += 1
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, game_id):
        ratings = Ratings.objects.filter(game=game_id)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, rating_id):
        try:
            rating = Ratings.objects.get(id=rating_id)
            serializer = RatingSerializer(rating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({f"error: {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, rating_id):
        try:
            rating = Ratings.objects.get(id=rating_id)
            rating.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ratings.DoesNotExist:
            return Response({"error": "Game Not Found"}, status=status.HTTP_404_NOT_FOUND)

class UserRegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')

        if password != password_confirm:
            return Response({"error": "The passwords do not match!"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "The username already exists!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.create_user(username=username, password=password)
            return Response({"message": "Account created successfully!"}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
            # return Response({"message: Login Successful"}, status=status.HTTP_200_OK)
        return Response({"Error: Wrong username or password. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            if "password" in request.data:
                user.set_password(request.data["password"])
                user.save()
            serializer.save()
            return Response({"message: Account data changed successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
def index(request):
    return render(request, "index.html")