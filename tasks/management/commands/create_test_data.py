from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from tasks.models import Task

class Command(BaseCommand):
    help = 'Creates test data for Task Manager'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create_user(username='john', password='test123')
        user2 = User.objects.create_user(username='alice', password='test123')
        user3 = User.objects.create_user(username='bob', password='test123')

        # Create test tasks
        task1 = Task.objects.create(
            title='Complete Project Documentation',
            description='Write comprehensive documentation for the new features',
            created_at=timezone.now(),
            status=False
        )
        task1.assigned_users.add(user1, user2)

        task2 = Task.objects.create(
            title='Bug Fix: Login System',
            description='Fix authentication issues in the login module',
            created_at=timezone.now(),
            status=True,
            completed_at=timezone.now(),
            completed_by=user1
        )
        task2.assigned_users.add(user2)

        task3 = Task.objects.create(
            title='Database Optimization',
            description='Optimize database queries for better performance',
            created_at=timezone.now(),
            status=False
        )
        task3.assigned_users.add(user1, user2, user3)

        self.stdout.write(self.style.SUCCESS('Successfully created test data'))
