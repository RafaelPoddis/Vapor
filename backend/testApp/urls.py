from django.urls import path
from . import views

app_name = "vapor"
urlpatterns = [
    path("", views.index, name="index"), # Pagina inicial
    # Games #
    path("games/", views.GameView.as_view(), name="create"), # Pagina para postar um jogo
    path("games/", views.GameView.as_view(), name="read"), # Pagina para mostrar os jogos
    path("games/<str:game_id>/", views.GameView.as_view(), name="update"), # Pagina para Atualizar um jogo
    path("games/<str:game_id>/", views.GameView.as_view(), name="delete"), # Pagina para remoover um jogo
    path("games/<str:game_id>/detail", views.GameDetail.as_view(), name="detail"), # Pagina do jogo
    # Ratings #
    path("games/<str:game_id>/ratings", views.RatingsView.as_view(), name="createRating"), # Postar avaliação de um jogo
    path("games/<str:game_id>/ratings", views.RatingsView.as_view(), name="readRating"), # Ler avaliações de um jogo
    path("ratings/<int:rating_id>", views.RatingsView.as_view(), name="updateRating"), # Atualizar Avaliação
    path("ratings/<int:rating_id>", views.RatingsView.as_view(), name="deleteRating"), # Deletar avaliação
    # Users #
    path("user/", views.UserRegisterView.as_view(), name="createUser"), # Criar usuario
    path("user/authenticate/", views.UserView.as_view(), name="createUser"), # Autenticar usuario
    path("user/<str:id>/", views.UserView.as_view(), name="readUser"), # Ver o perfil do usuario
    path("user/<str:id>/", views.UserView.as_view(), name="updateUser"), # Atualizar dados de usuario
    path("user/<str:id>/", views.UserView.as_view(), name="deleteUser"), # Atualizar dados de usuario
]