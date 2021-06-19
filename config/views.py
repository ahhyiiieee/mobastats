from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from players import models as players_models


@login_required
def home(request):
    last_5_games = players_models.Game.objects.all().order_by('-date')[:5]
    player_top_5_heroes = players_models.PlayerHero.objects.all().order_by('-num_games')[:5]
    #top_5_heroes =

    context = {
        'player': request.user,
        'last_5_games': last_5_games,
        'player_top_5_heroes': player_top_5_heroes,
    }
    return render(request, 'home.html', context)
