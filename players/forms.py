from django.forms import ModelForm
from django.utils import timezone
from django.forms.fields import DateTimeField
from django import forms

from .models import Game


# creating a form for recording games
class LatestGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'hero',
            'result',
            'kills',
            'deaths',
            'assists',
            'date',
            'duration'
        ]