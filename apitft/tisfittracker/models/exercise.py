from django.db import models

from .machineExercise import MachineExercise
from .series import Serie
from .machine import Machine


class Exercise(models.Model):
    imgName = models.ImageField(upload_to="exercise/")
    rest = models.FloatField()
    machine = models.OneToOneField(Machine, on_delete=models.DO_NOTHING)
    machineExercise = models.OneToOneField(MachineExercise, on_delete=models.DO_NOTHING)
    serie = models.ManyToManyField(Serie, related_name="machine_exercise")
