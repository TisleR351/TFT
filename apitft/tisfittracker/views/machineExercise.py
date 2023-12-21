from rest_framework import viewsets
from ..models import MachineExercise
from ..serializers import MachineExerciseSerializer


class MachineExerciseViewSet(viewsets.ModelViewSet):
    queryset = MachineExercise.objects.all()
    serializer_class = MachineExerciseSerializer
