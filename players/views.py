from django.http import request
from django.shortcuts import redirect, render
from django.utils import timezone
from django.forms import formset_factory

from .models import Player, PlayerHero, Game, Hero, GamePlayer
from .forms import GamePlayerForm, GameForm

# 1. Make sure to place your exception handler as close to the source of the exception as possible
# 2. In general, don't write too long functions. See if you can extract distinct pieces of logic into their own functions 

# Create your views here.
def latest_game_form(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        game_player_form = GamePlayerForm(request.POST)
        w_formset = WinnerFormSet(request.POST)

        if game_form.is_valid() and game_player_form.is_valid():
            game = game_form.save(commit=True)
            game_player = game_player_form.save(commit=False)
            game_player.game = game
            game_player.save()

            #For Updating PlayerHero and Hero Models
            PlayerHero.update_stats(game_player.player, game_player.hero)
            Hero.update_stats(game_player.hero)

            return redirect('home')

    else:

        game_form = GameForm(initial={'date': timezone.now()})
        game_player_form = GamePlayerForm()

        GamePlayerFormSet = formset_factory(GamePlayerForm, extra=5, max_num=5, min_num=None)
        winner_formset = GamePlayerFormSet()
        loser_formset = GamePlayerFormSet()

        context = {
            'game_form': game_form,
            #'game_player_form': game_player_form,
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