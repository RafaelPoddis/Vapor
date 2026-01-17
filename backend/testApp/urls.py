from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "vapor"
urlpatterns = [
    path("", views.index, name="index"), # Pagina inicial
    # Games #
    path("games/", views.GameView.as_view(), name="create"), # Pagina para postar um jogo
    path("games/", views.GameView.as_view(), name="read"), # Pagina para mostrar os jogos
    path("games/<str:game_id>/", views.GameView.as_view(), name="update"), # Pagina para Atualizar um jogo
    path("games/<str:game_id>/", views.GameView.as_view(), name="delete"), # Pagina para remoover um jogo
    path("games/<str:game_id>/detail", views.GameDetail.as_view(), name="detail"), # Pagina do jogo
    path("games/<str:game_id>/buy", views.GameDetail.as_view(), name="buyGame"), # Compra do jogo
    # Ratings #
    path("games/<str:game_id>/ratings", views.RatingsView.as_view(), name="createRating"), # Postar avaliação de um jogo
    path("games/<str:game_id>/ratings", views.RatingsView.as_view(), name="readRating"), # Ler avaliações de um jogo
    path("ratings/<int:rating_id>", views.RatingsView.as_view(), name="updateRating"), # Atualizar Avaliação
    path("ratings/<int:rating_id>", views.RatingsView.as_view(), name="deleteRating"), # Deletar avaliação
    # Users #
    path("user/", views.UserRegisterView.as_view(), name="createUser"), # Criar usuario
    path("user/authenticate/", views.UserView.as_view(), name="authUser"), # Autenticar usuario
    path("user/<str:id>/", views.UserView.as_view(), name="readUser"), # Ver o perfil de um usuario
    path("user/<str:id>/", views.UserView.as_view(), name="updateUser"), # Atualizar dados de usuario
    path("user/<str:id>/", views.UserView.as_view(), name="deleteUser"), # Atualizar dados de usuario
    path("users/", views.GetAllUsers.as_view(), name="allUser"), # Ver todos os usuarios
    path("authenticateduser/", views.AuthenticatedUserView.as_view(), name="readMe"), # Ver dados do usuario autenticado
    # Genres #
    path("genres/", views.GenresViews.as_view(), name="createGenres"), # Criar gênero
    path("genres/", views.GenresViews.as_view(), name="readGenres"), # Ler gênero
    path("genres/<str:id>/", views.GenresViews.as_view(), name="updateGenres"), # Atualizar gênero
    path("genres/<str:id>/", views.GenresViews.as_view(), name="deleteGenres"), # Deletar gênero
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)