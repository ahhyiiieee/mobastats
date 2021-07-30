from rest_framework import serializers
from .models import Hero, PlayerHero, Game, GamePlayer, Player


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class PlayerHeroSerializer(serializers.ModelSerializer):
    # hero_display = HeroSerializer(source='hero', read_only=True)
    # hero_name = serializers.CharField(source='hero')

    class Meta:
        model = PlayerHero
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    # player_heroes = PlayerHeroSerializer('player_heroes', many=True, read_only=True)
    top_5_heroes = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = [
            'id',
            'username',
            'display_name',
            'top_5_heroes',
        ]

    def get_top_5_heroes(self, obj):
        top_5_heroes = obj.player_heroes.order_by('-winrate', '-num_games', 'hero__name')[:5]
        return PlayerHeroSerializer(top_5_heroes, many=True).data


class GamePlayerSerializer(serializers.ModelSerializer):
    # player_data = PlayerSerializer(source='player', read_only=True)
    class Meta:
        model = GamePlayer
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    game_players = GamePlayerSerializer('game_players', many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
