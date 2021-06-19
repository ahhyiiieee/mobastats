from django import forms
from django.utils import timezone
from django.forms.fields import DateTimeField

from .models import Game


# creating a form for recording games
# result choices

class LatestGameForm(forms.Form):
    hero = forms.CharField()
    result = forms.CharField(label='Result', widget=forms.Select(choices=Game.RESULT_TYPES))
    kills = forms.IntegerField()
    deaths = forms.IntegerField()
    assists = forms.IntegerField()
    date = forms.DateTimeField(initial=timezone.now())
    duration = forms.TimeField()
