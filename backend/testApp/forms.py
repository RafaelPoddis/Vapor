from django import forms
from .models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'

        isAdults = forms.ChoiceField(
        choices=[(False, "For Everyone"), (True, "Adults Only")],
        widget=forms.RadioSelect()
        )

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
        }