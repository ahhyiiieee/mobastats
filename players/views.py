from django.shortcuts import redirect, render
from django.utils import timezone
from django.forms import modelformset_factory
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import action

from .serializers import GamePlayerSerializer, GameSerializer, HeroSerializer, PlayerSerializer, PlayerHeroSerializer
from .models import Player, PlayerHero, Game, Hero, GamePlayer
from .forms import GameForm, GamePlayerForm

# 1. Make sure to place your exception handler as close to the source of the exception as possible
# 2. In general, don't write too long functions
# See if you can extract distinct pieces of logic into their own functions


class DashboardViewSet(viewsets.ViewSet):
    def get_user(self):
        return self.request.user

    @action(detail=False, url_path='top-5-heroes')
    def top_5_heroes(self, request):
        queryset = PlayerHero.objects.filter(player=request.user, num_games__gte=1).order_by(
            '-winrate', '-num_games', 'hero__name'
        )[:5]
        serializer = PlayerHeroSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='top-5-heroes-global')
    def top_5_heroes_global(self):
        queryset = Hero.objects.filter(num_games__gte=1).order_by('-winrate', '-num_games', 'name')[:5]
        serializer = HeroSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='last-5-games')
    def last_5_games(self, request):
        queryset = GamePlayer.objects.filter(player=request.user).order_by('-game__date')[:5]
        serializer = GamePlayerSerializer(queryset, many=True)
        return Response(serializer.data)


class GamePlayerViewSet(viewsets.ModelViewSet):
    queryset = GamePlayer.objects.all()
    serializer_class = GamePlayerSerializer
    filterset_fields = ['player']


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

# class PlayerViewSet(viewsets.ModelViewSet):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer


# class PlayerHeroViewSet(viewsets.ModelViewSet):
#     queryset = PlayerHero.objects.all()
#     serializer_class = PlayerHeroSerializer


def latest_game_form(request):
    game_form = GameForm(initial={'date': timezone.now()})
    GamePlayerFormSet = modelformset_factory(GamePlayer, form=GamePlayerForm, extra=5)
    winner_formset = GamePlayerFormSet(
        queryset=GamePlayer.objects.none(), initial=[{'game': game_form}], prefix='winner',
    )
    loser_formset = GamePlayerFormSet(
        queryset=GamePlayer.objects.none(), initial=[{'game': game_form}], prefix='loser',
    )
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        winner_formset = GamePlayerFormSet(request.POST, prefix='winner')
        loser_formset = GamePlayerFormSet(request.POST, prefix='loser')
        if game_form.is_valid():
            game = game_form.save()
        if winner_formset.is_valid():
            instances = winner_formset.save(commit=False)
            for instance in instances:
                instance.game = game
                instance.save()
                PlayerHero.update_stats(instance.player, instance.hero)
                Hero.update_stats(instance.hero)
        if loser_formset.is_valid():
            instances = loser_formset.save(commit=False)
            for instance in instances:
                instance.game = game
                instance.save()
                PlayerHero.update_stats(instance.player, instance.hero)
                Hero.update_stats(instance.hero)

        return redirect('home')
    else:
        print(game_form.errors, winner_formset.errors)

    context = {
        'game_form': game_form,
        'winner_formset': winner_formset,
        'loser_formset': loser_formset,
        }

    return render(request, 'players/latest_game_form.html', context)


def game_details(request, pk):
    games = Game.objects.get(pk=pk)

    context = {
        'games': games,
    }

    return render(request, 'players/game_details.html', context)


def player_details(request, pk):
    players = Player.objects.get(pk=pk)
    player_games = players.gameplayer_set.order_by('-game__date')

    context = {
        'players': players,
        'player_games': player_games,
        }

    return render(request, 'players/player_details.html', context)
