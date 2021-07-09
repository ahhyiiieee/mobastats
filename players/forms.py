from django.forms import ModelForm
from django.utils import timezone
from django.forms.fields import DateTimeField
from django import forms

from .models import GamePlayer, Game


# creating a form for recording games
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'date',
            'duration',
        ]
        

class GamePlayerForm(forms.Form):
    WIN = 1
    LOST = 2
    INVALID = 3

    RESULT_TYPES = [
        (WIN, 'Win'),
        (LOST, 'Lost'),
        (INVALID, 'Invalid'),
    ]

    BLUE = 1
    RED = 2

    TEAM_SIDE = [
        (BLUE,'Blue'),
        (RED,'Red'),
    ]

    team = forms.CharField(widget=forms.Select(choices=RESULT_TYPES))
    result = forms.CharField(widget=forms.Select(choices=TEAM_SIDE))
    player = forms.CharField()
    hero = forms.CharField()
    kills = forms.IntegerField()
    deaths = forms.IntegerField()
    assists = forms.IntegerField()

#make another form for game
#then render the 2 forms together
#1 Game form, 10 GamePlayer forms later task

