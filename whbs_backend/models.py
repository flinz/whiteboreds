from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


# Games
class Game(models.Model):
    game_date = models.DateField()  # game creation
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Game <%s | %s>" % (self.game_date, self.player)


# Scores for players
class Score(models.Model):

    # Links to internal models
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    # coordinates
    r = models.FloatField(blank=True, null=True)
    phi = models.FloatField(blank=True, null=True)

    # calculated score
    score = models.IntegerField(default=0)

    # player turn
    turn = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Score <%s | %s>" % (self.game, self.player)
