from django.shortcuts import render, redirect
from .forms import GamesForm
from .models import Games

# Create your views here.
def gamesFormView(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vapor:show_url")
        else:
            print(form.errors)
    template = 'forms.html'
    context = {'form':form}
    return render(request, template, context)

def showView(request):
    obj = Games.objects.all()
    template_name = 'show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateView(request, name):
    obj = Games.objects.get(name=name)
    form = GamesForm(instance=obj)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("vapor:show_url")
    template_name = 'forms.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, name):
    obj = Games.objects.get(name=name)
    if request.method == 'POST':
        obj.delete()
        return redirect('vapor:show_url')
    template_name = 'confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def index(request):
    return render(request, "index.html")