from django.contrib import admin

from tisfittracker.models import (
    Exercise,
    MachineExercise,
    Machine,
    Serie,
    Workout,
)

admin.site.register(Exercise)
admin.site.register(MachineExercise)
admin.site.register(Machine)
admin.site.register(Serie)
admin.site.register(Workout)
