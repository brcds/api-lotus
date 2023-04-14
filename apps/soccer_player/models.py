from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Player(models.Model):
    name = models.TextField()
    date_of_birth = models.DateField()
    number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    position = models.TextField()

