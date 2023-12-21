from django.db import models

from .utils import Difficulty


class Serie(models.Model):
    name = models.CharField(max_length=100, default="Serie")
    weight = models.FloatField()
    repetitions = models.IntegerField()
    difficulty = models.CharField(
        max_length=100,
        choices=[(tag.name, tag.value) for tag in Difficulty],
        default=Difficulty.MOYEN.value,
    )
