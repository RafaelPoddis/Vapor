from django import forms
from .models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'

        contentRating = {"0":"ForEveryone", "1":"AdultsOnly"}

        labels = {
            'name' : 'Game Name',
            'price' : 'Price',
            'description' : 'Game Description',
            'isAdults' :  'Is for Adults Only?'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'The Game'}),
            'price' : forms.NumberInput(attrs={'placeholder': '0,00'}),
            'description' : forms.Textarea(attrs={'placeholder': 'This is a 2D game...'}),
            'isAdults' : forms.RadioSelect(choices=contentRating),
        }