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


class PlayerHero(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    winrate = models.DecimalField(max_digits=4, decimal_places=1)
    num_games = models.IntegerField()

    def __str__(self):
        return f'{self.player} - {self.hero}'


class Game(models.Model):
    WIN = 1
    LOST = 2
    INVALID = 3

    RESULT_TYPES = [
        (WIN, 'Win'),
        (LOST, 'Lost'),
        (INVALID, 'Invalid'),
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField(choices=RESULT_TYPES)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    date = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.player} - {self.hero} ({self.date})'
