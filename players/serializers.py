from rest_framework import serializers
from .models import Hero, PlayerHero, Game, GamePlayer


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class PlayerHeroSerializer(serializers.ModelSerializer):
    hero_display = HeroSerializer(source='hero', read_only=True)

    class Meta:
        model = PlayerHero
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GamePlayerSerializer(serializers.ModelSerializer):
    game_data = GameSerializer(source='game', read_only=True)
    team_display = serializers.CharField(source='get_team_display', read_only=True)
    result_display = serializers.CharField(source='get_result_display', read_only=True)

    class Meta:
        model = GamePlayer
        fields = '__all__'
