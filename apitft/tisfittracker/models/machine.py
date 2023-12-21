from django.db import models

from .machineExercise import MachineExercise


class Machine(models.Model):
    name = models.CharField(max_length=100)
    imgName = models.ImageField(upload_to="machine/")
    machineExercise = models.ManyToManyField(
        MachineExercise, related_name="machine_exercise"
    )
