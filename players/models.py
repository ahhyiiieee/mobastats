from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)


class Hero(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
         return self.name 
	winrate = models.DecimalField(max_digits=3,decimal_places=1)
	num_games = models.IntegerField()


class PlayerHero(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
	winrate = models.DecimalField(max_digits=3,decimal_places=1)
	num_games =  models.IntegerField()
	

class Game(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
	result = models.IntegerField()
	kills = models.IntegerField()
	deaths = models.IntegerField()
	assists = models.IntegerField()
	date = models.DateTimeField()
	duration = models.TimeField()