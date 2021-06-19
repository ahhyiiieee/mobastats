from django.shortcuts import render
from .models import *
from .forms import LatestGameForm


# Create your views here.
def latest_game_form(request):
    context = {}
    context['form'] = LatestGameForm()
    return render(request, 'players/latest_game_form.html', context)