from django.contrib.auth.models import User
admin_user = User.objects.get(username='admin')
admin_user.set_password('123')
admin_user.save()
