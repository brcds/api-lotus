from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Match(models.Model):
    adversary = models.TextField()
    location = models.TextField()
    game_date = models.DateField()
    game_time = models.IntegerField(
         validators=[MinValueValidator(0), MaxValueValidator(23)]
    )
    #result
