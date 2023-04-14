from django.db import models

# Create your models here.

class GameResult(models.Model):
    lotus_goal = models.IntegerField()
    opponent_goal = models.IntegerField()
    #player_scored


