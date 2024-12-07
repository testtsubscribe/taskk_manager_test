from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **kwargs):
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        admin_group = Group.objects.get(name='admin')
        admin_user.groups.add(admin_group)
        self.stdout.write('Successfully created admin user')
