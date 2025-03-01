from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("algo", views.greet, name="greet"),
    path("homepage", views.home, name="home"),
]