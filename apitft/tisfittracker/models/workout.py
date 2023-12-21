from django.db import models
from django.contrib.auth.models import User

from .exercise import Exercise
from .utils import Type, Difficulty


class Workout(models.Model):
    type = models.CharField(
        max_length=100, choices=[(tag.name, tag.value) for tag in Type]
    )
    imgName = models.ImageField(upload_to="workout/")
    date = models.DateField()
    time = models.FloatField()
    difficulty = models.CharField(
        max_length=100,
        choices=[(tag.name, tag.value) for tag in Difficulty],
        default=Difficulty.MOYEN.value,
    )
    exercise = models.ManyToManyField(
        Exercise, related_name="exercise", blank=True
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
