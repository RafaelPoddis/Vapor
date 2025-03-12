from django.shortcuts import render, redirect
from .forms import GamesForm
from .models import Games

games = ['Game 1', 'Game 2', 'Game 3']
# Create your views here.
def gamesFormView(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template = 'forms.html'
    context = {'form':form}
    return render(request, template, context)

def showView(request):
    obj = Games.objects.all()
    template_name = 'show.html'
    context = {'games': games}
    return render(request, template_name, context)

def updateView(request, f_name):
    obj = Games.objects.get(name=f_name)
    form = GamesForm(instance=obj)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'forms.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_name):
    obj = Games.objects.get(name=f_name)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'index.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def index(request):
    return render(request, "index.html")