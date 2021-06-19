from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)


class Hero(models.Model):
    name = models.CharField(max_length=30, null=True)
    winrate = models.DecimalField(max_digits=3, decimal_places=1)
    num_games = models.IntegerField()

    def __str__(self):
        return self.name


class PlayerHero(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    winrate = models.DecimalField(max_digits=3, decimal_places=1)
    num_games = models.IntegerField()


class Game(models.Model):
    WIN = 'Win'
    LOSS = 'Loss'
    INVALID = 'Invalid'

    RESULT_TYPES = [
        (1, WIN),
        (2, LOSS),
        (3, INVALID),
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField(choices=RESULT_TYPES)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    date = models.DateTimeField()
    duration = models.TimeField()
