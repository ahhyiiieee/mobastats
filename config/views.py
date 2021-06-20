from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from players import models as players_models


@login_required
def home(request):
    game = players_models.Game.objects.all()

    """
    num_games_won = game.filter(player=request.user,result=1).count()
    num_games_lost = game.filter(player=request.user,result=2).count()
    num_games = num_games_won + num_games_lost
    win_rate = num_games_won / num_games * 100
    """

    last_5_games = game.filter(player=request.user).order_by('-date')[:5]
    player_top_5_heroes = players_models.PlayerHero.objects.all().filter(player=request.user).order_by('-winrate')[:5]
    #top_5_heroes =

    context = {
        'player': request.user,
        'last_5_games': last_5_games,
        'player_top_5_heroes': player_top_5_heroes,
    }
    return render(request, 'home.html', context)
