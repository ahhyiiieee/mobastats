from rest_framework import serializers
from .models import Hero, PlayerHero, Game, GamePlayer, Player


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class PlayerHeroSerializer(serializers.ModelSerializer):
    # hero_display = HeroSerializer(source='hero', read_only=True)

    class Meta:
        model = PlayerHero
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'id',
            'display_name',
        ]


class GamePlayerSerializer(serializers.ModelSerializer):
    player_data = PlayerSerializer(source='player', read_only=True)

    class Meta:
        model = GamePlayer
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    game_players = GamePlayerSerializer(source='gameplayer_set', many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
