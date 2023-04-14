from django.db import models
from apps.game_result.models import GameResult


class Score(models.Model):
  player = models.TextField()
  goal = models.IntegerField()
  game_result = models.TextField()
