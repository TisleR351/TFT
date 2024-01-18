from django.dispatch import receiver
from django.contrib.auth.models import Group
from rest_registration.signals import user_registered


@receiver(user_registered)
def assign_group_to_new_user(user, **kwargs):
    group_name = "BaseUser"
    group = Group.objects.get(name=group_name)
    user.groups.add(group)
