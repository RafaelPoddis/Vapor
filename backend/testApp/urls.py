from django.urls import path
from . import views

urlpatterns = [
    path("", views.gamesFormView, name="index"),
    path("show_url", views.showView, name="show_url"),
]