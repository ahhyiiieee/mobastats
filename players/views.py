from django.http import request
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import PlayerHero, Game, Hero, GamePlayer
from .forms import GamePlayerForm, GameForm

# 1. Make sure to place your exception handler as close to the source of the exception as possible
# 2. In general, don't write too long functions. See if you can extract distinct pieces of logic into their own functions 

# Create your views here.
def latest_game_form(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        game_player_form = GamePlayerForm(request.POST)

        if game_form.is_valid() and game_player_form.is_valid():
            game = game_form.save(commit=False)
            game_player = game_player_form.save(commit=False)
            game_player.player = request.user
            game_player.game = game
            game.save()
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

        
        #PlayerHero.update_stats(game.player, game.hero)
        #Hero.update_stats(game.hero)


def game_details(request):
    game = Game.objects.all()
    hero = Hero.objects.all()
    game_players = PlayerHero.objects.all()
    all_games = game_players.filter(player=request.user)
    
    context = {
        'player': request.user,
        'all_games': all_games,
    }

    return render(request, 'players/game_details.html', context)


def player_details(request):
    context = {'player': request.user,}
    return render(request, 'players/player_details.html', context)