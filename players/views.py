from django.http import request
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import PlayerHero, Game, Hero
from .forms import LatestGameForm



# Create your views here.
def latest_game_form(request):
    if request.method == 'POST':
        form = LatestGameForm(request.POST)
        if form.is_valid():
            try:
                game = form.save(commit=False)
                game.player = request.user
                game.save()    
                num_games_won = Game.objects.filter(
                    player=game.player,
                    result=Game.WIN,
                    hero=game.hero,
                ).count()
                num_games_lost = Game.objects.filter(
                    player=game.player,
                    result=Game.LOST,
                    hero=game.hero,
                ).count()
                num_games = num_games_won + num_games_lost
                winrate = (num_games_won / num_games) * 100
                PlayerHero.objects.update_or_create(
                    player=game.player,
                    hero=game.hero,
                    defaults={
                        'winrate': winrate,
                        'num_games': num_games,
                    }
                )
                global_num_games_won = Game.objects.filter(
                    result=Game.WIN,
                    hero=game.hero,
                ).count()
                global_num_games_lost = Game.objects.filter(
                    result=Game.LOST,
                    hero=game.hero,
                ).count()
                global_num_games = global_num_games_won + global_num_games_lost
                global_winrate = (global_num_games_won / global_num_games) * 100
                hero = game.hero
                hero.num_games = global_num_games
                hero.winrate = global_winrate
                hero.save()
                return redirect('home')
            except ZeroDivisionError:
                return redirect('home')
    else:
        form = LatestGameForm(initial={'date': timezone.now()})
        context = {
            'form':form,
        }
        return render(request, 'players/latest_game_form.html', context)