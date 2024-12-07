from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name='admin')
        Group.objects.get_or_create(name='standard_user')
        self.stdout.write('Successfully created groups')