from django.forms import ModelForm
from django.utils import timezone
from django.forms.fields import DateTimeField
from django import forms

from .models import GamePlayer, Game


# creating a form for recording games
class GamePlayerForm(forms.ModelForm):
    class Meta:
        model = GamePlayer
        fields = [
            'team',
            'result',
            'player',
            'hero',
            'kills',
            'deaths',
            'assists',
        ]


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'date',
            'duration',
        ]
        
#make another form for game
#then render the 2 forms together
#1 Game form, 10 GamePlayer forms later task

