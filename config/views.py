from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from players import models as players_models


@login_required
def home(request):
    game = players_models.Game.objects.all()
    hero = players_models.Hero.objects.all()
    game_players = players_models.GamePlayer.objects.all()
    last_5_games = game_players.filter(player=request.user).order_by('-game')[:5]
    
    #Cannot resolve keyword 'gameplayer' into field 
    #last_5_games = game_players.filter(gameplayer__player=request.user).order_by('-game')[:5]
    player_top_5_heroes = players_models.PlayerHero.objects.all().filter(player=request.user, num_games__gte=1).order_by('-winrate', '-num_games', 'hero__name')[:5]
    top_5_heroes = hero.filter(num_games__gte=1).order_by('-winrate', '-num_games', 'name')[:5]

    context = {
        'player': request.user,
        'last_5_games': last_5_games,
        'player_top_5_heroes': player_top_5_heroes,
        'top_5_heroes': top_5_heroes,
    }
    return render(request, 'home.html', context)