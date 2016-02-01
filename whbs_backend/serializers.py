from django.contrib.auth.models import User
from whbs_backend.models import Game, Score
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'player', 'game_date', 'score_set')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'player', 'game', 'r', 'phi', 'score', 'turn')
