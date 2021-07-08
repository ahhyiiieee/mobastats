from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)


class Hero(models.Model):
    name = models.CharField(max_length=30)
    winrate = models.DecimalField(max_digits=4, decimal_places=1)
    num_games = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def update_stats(cls, hero):
        global_num_games_won = GamePlayer.objects.filter(
            result=GamePlayer.WIN,
            hero=hero,
        ).count()
        global_num_games_lost = GamePlayer.objects.filter(
            result=GamePlayer.LOST,
            hero=hero,
        ).count()
        global_num_games = global_num_games_won + global_num_games_lost
        try:
            global_winrate = (global_num_games_won / global_num_games) * 100
        except ZeroDivisionError:
            global_winrate = 0
        hero = hero
        hero.num_games = global_num_games
        hero.winrate = global_winrate
        hero.save()


class PlayerHero(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    winrate = models.DecimalField(max_digits=4, decimal_places=1)
    num_games = models.IntegerField()

    def __str__(self):
        return f'{self.player} - {self.hero}'

    @classmethod
    def update_stats(cls, player, hero):
        num_games_won = GamePlayer.objects.filter(
            player=player,
            result=GamePlayer.WIN,  
            hero=hero,
        ).count()
        num_games_lost = GamePlayer.objects.filter(
            player=player,
            result=GamePlayer.LOST,
            hero=hero,
        ).count()
        num_games = num_games_won + num_games_lost
        try:
            winrate = (num_games_won / num_games) * 100
        except ZeroDivisionError:
            winrate = 0
        PlayerHero.objects.update_or_create(
            player=player,
            hero=hero,
            defaults={
                'winrate': winrate,
                'num_games': num_games,
            }
        )


class Game(models.Model):
    date = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.date} - {self.duration}'


class GamePlayer(models.Model):
    WIN = 1
    LOST = 2
    INVALID = 3

    RESULT_TYPES = [
        (WIN, 'Win'),
        (LOST, 'Lost'),
        (INVALID, 'Invalid'),
    ]

    BLUE = 1
    RED = 2

    TEAM_SIDE = [
        (BLUE,'Blue'),
        (RED,'Red'),
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField(choices=RESULT_TYPES)
    team = models.PositiveSmallIntegerField(choices=TEAM_SIDE)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    
    def __str__(self):
        return f'{self.player} - {self.hero} - {self.team}'
        
# A game can involve 10 players, and they don't have to enter their own game if someone else entered it.

'''
1. Separate entry for all players: Hero, K/D/A.
2. 2 groups of 5, winning side and losing side

Break down the Game model into two models, 
Game (containing date and duration) and 
GamePlayer (foreign keys to Game and Player, and hero/result/kda). 
The goal is to be able to enter one game that ties to multiple players.
'''