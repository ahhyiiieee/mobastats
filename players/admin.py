from django.contrib import admin
from .models import Player, Hero, PlayerHero, Game, GamePlayer

admin.site.register(Player)
admin.site.register(Hero)
admin.site.register(PlayerHero)
admin.site.register(Game)
admin.site.register(GamePlayer)
