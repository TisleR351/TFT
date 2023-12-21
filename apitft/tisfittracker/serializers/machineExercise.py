from rest_framework import serializers
from ..models import MachineExercise


class MachineExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineExercise
        fields = ["id", "name", "imgName"]
