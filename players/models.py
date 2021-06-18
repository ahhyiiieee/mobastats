from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)


class Hero(models.Model):
	name = models.CharField(max_length=30,null=True)
	def __str__(self):
         return self.name 
	winrate = models.DecimalField(max_digits=3,decimal_places=1)
	num_games = models.IntegerField()


class PlayerHero(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE,null=True)
	hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
	winrate = models.DecimalField(max_digits=3,decimal_places=1)
	num_games =  models.IntegerField()
	

class Game(models.Model):
	GAME_RESULT=[(1,'Win'),(2,'Loss'),(3,'Invalid')]

	player = models.ForeignKey(Player, on_delete=models.CASCADE,null=True)
	hero = models.ForeignKey(PlayerHero, on_delete=models.CASCADE,null=True)
	result = models.CharField(max_length=200, null=True, choices=GAME_RESULT)
	kills = models.IntegerField()
	deaths = models.IntegerField()
	assists = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True,null=True)
	duration = models.TimeField()