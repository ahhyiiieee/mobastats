from django.db.models.query import QuerySet
from django.forms.models import ModelMultipleChoiceField
from django.http import request
from django.shortcuts import redirect, render
from django.utils import timezone
from django.forms import fields

from .models import Player, PlayerHero, Game, Hero, GamePlayer
from .forms import GameForm, GamePlayerFormSet

# 1. Make sure to place your exception handler as close to the source of the exception as possible
# 2. In general, don't write too long functions. See if you can extract distinct pieces of logic into their own functions 

# Create your views here.
def latest_game_form(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        winner_formset = GamePlayerFormSet(request.POST)
        if game_form.is_valid() and winner_formset.is_valid():
            game = game_form.save()
            instances = winner_formset.save(commit=False)
            for instance in instances:
                instance.game = game
                instance.save()
                instance.result = GamePlayer.WIN
                PlayerHero.update_stats(instance.player, instance.hero)
                Hero.update_stats(instance.hero)
                return redirect('home')
                    
    game_form = GameForm(initial={'date': timezone.now()})
    winner_formset = GamePlayerFormSet(queryset=GamePlayer.objects.none())
    loser_formset = GamePlayerFormSet(queryset=GamePlayer.objects.none())              
    
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