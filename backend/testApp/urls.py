from django.urls import path
from . import views

app_name = "vapor"
urlpatterns = [
    path("", views.index, name="index"),
    path("creategame/", views.GameView.as_view(), name="create"),
    path("showgames/", views.GameView.as_view(), name="read"),
    path("game/<str:gameName>/update/", views.GameView.as_view(), name="update"),
    path("game/<str:gameName>/delete/", views.GameView.as_view(), name="delete"),
    path("game/<str:gameName>/", views.GameDetail.as_view(), name="detail"),
]