from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_group_with_permissions(group_custom_name, permissions, content_type_mapping_from_codename):
    group, created = Group.objects.get_or_create(name=group_custom_name)

    for permission in permissions:
        codename_parts = permission["codename"].split("_")
        model_name = codename_parts[-1]
        content_type_id = content_type_mapping_from_codename.get(model_name)
        permission["content_type_id"] = content_type_id
        perm, _ = Permission.objects.get_or_create(
            content_type_id=permission['content_type_id'],
            codename=permission['codename'],
            name=permission['name'],
        )
        group.permissions.add(perm.id)

    group.save()


group_name = "BaseUser"
permissions_base_user = [
    {"name": "Can view my workout", "codename": "view_self_workout"},
    {"name": "Can view my exercise", "codename": "view_self_exercise"},
    {"name": "Can view my series", "codename": "view_self_serie"},
    {"name": "Can view machine", "codename": "view_machine"},
    {"name": "Can view machine exercise", "codename": "view_machineexercise"},
    {"name": "Can delete my workout", "codename": "delete_self_workout"},
]

group_name_moderator = "Moderator"
permissions_moderator = [
    {"name": "Can view workout", "codename": "view_workout"},
    {"name": "Can view exercise", "codename": "view_exercise"},
    {"name": "Can view serie", "codename": "view_serie"},
    {"name": "Can add machine", "codename": "add_machine"},
    {"name": "Can add machine exercise", "codename": "add_machineexercise"},
    {"name": "Can delete workout", "codename": "delete_workout"},
]

content_type_mapping = {
    content_type.model: content_type.id
    for content_type in ContentType.objects.all()
}

create_group_with_permissions(group_name, permissions_base_user, content_type_mapping)
create_group_with_permissions(group_name_moderator, permissions_base_user, content_type_mapping)
create_group_with_permissions(group_name_moderator, permissions_moderator, content_type_mapping)

exit()
