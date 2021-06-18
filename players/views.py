from django.shortcuts import render
from .models import *
from .forms import LatestGameForm

# Create your views here.
def latestGame(request):
    context = {}
    context['form'] = LatestGameForm()
    return render(request, 'players/latest_game.html', context)


def last_5_games(request):
    last_5_games = Game.object.all()

    return render(request, 'home.html', {'last_5_games':last_5_games})
