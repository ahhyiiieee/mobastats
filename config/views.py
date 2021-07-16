from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

from players import models as players_models


class TestView(APIView):
    def get(self, request):

        return Response('asd')


@login_required
def home(request):
    game_players = players_models.GamePlayer.objects.all()
    player_heroes = players_models.PlayerHero.objects.all()
    hero = players_models.Hero.objects.all()

    last_5_games = game_players.filter(
        player=request.user).order_by('-game__date')[:5]
    player_top_5_heroes = player_heroes.filter(
        player=request.user, num_games__gte=1).order_by('-winrate', '-num_games', 'hero__name')[:5]
    top_5_heroes = hero.filter(num_games__gte=1).order_by('-winrate', '-num_games', 'name')[:5]

    context = {
        'last_5_games': last_5_games,
        'player_top_5_heroes': player_top_5_heroes,
        'top_5_heroes': top_5_heroes,
    }

    return render(request, 'home.html', context)
