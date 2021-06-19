from django.shortcuts import render
from .models import *
from .forms import LatestGameForm

# Create your views here.
def latestGame(request):
    context = {}
    context['form'] = LatestGameForm()
    return render(request, 'players/latest_game.html', context)