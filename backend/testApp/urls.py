from django.urls import path
from . import views

app_name = "vapor"
urlpatterns = [
    path("", views.index, name="index"),
    path("forms/", views.gamesFormView, name="forms"),
    path("show_url/", views.showView, name="show_url"),
    path("update/<str:name>", views.updateView, name="update"),
    path("delete/<str:name>", views.deleteView, name="delete"),
]