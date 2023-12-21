from django.db import models


class MachineExercise(models.Model):
    name = models.CharField(max_length=100)
    imgName = models.ImageField(upload_to="machine_exercise/")
