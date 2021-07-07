from django.http import request
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Player, PlayerHero, Game, Hero, GamePlayer
from .forms import GamePlayerForm, GameForm

# 1. Make sure to place your exception handler as close to the source of the exception as possible
# 2. In general, don't write too long functions. See if you can extract distinct pieces of logic into their own functions 

# Create your views here.
def latest_game_form(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        game_player_form = GamePlayerForm(request.POST)

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
        context = {
            'game_form': game_form,
            'game_player_form': game_player_form,
        }
        return render(request, 'players/latest_game_form.html', context)


def game_details(request, pk):
    game_data = Game.objects.get(pk=pk)

    context = {
        'player': request.user,
        'game_data': game_data,
    }

    return render(request, 'players/game_details.html', context)


def player_details(request, pk):
    player_data = Player.objects.get(pk=pk)
    player_game_data = Game.objects.get(pk=pk)

    context = {
        'player': request.user,
        'player_game_data': player_game_data,
        'player_data': player_data,
        }
    return render(request, 'players/player_details.html', context)