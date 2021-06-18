from django import forms
from django.forms.fields import DateTimeField

#creating a form for recording games
#result choices
GAME_RESULT=[(1,'Win'),(2,'Loss'),(3,'Invalid')]

class LatestGameForm(forms.Form):
    hero = forms.CharField()
    result = forms.CharField(label='Result',widget=forms.Select(choices=GAME_RESULT))
    kills = forms.IntegerField()
    deaths = forms.IntegerField()
    assists = forms.IntegerField()
    date = forms.DateTimeField()
    duration = forms.TimeField()