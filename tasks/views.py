from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

@login_required
def task_list(request):
    if request.user.groups.filter(name='admin').exists():
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_users=request.user)
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'is_admin': request.user.groups.filter(name='admin').exists()
    })

@login_required
def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user.groups.filter(name='admin').exists() or request.user in task.assigned_users.all():
        task.status = True
        task.completed_at = timezone.now()
        task.completed_by = request.user
        task.save()
    return redirect('task_list')


def task_list(request):
    filter_param = request.GET.get('filter', 'all')
    
    # Base queryset filtered by user's assignments
    base_queryset = Task.objects.filter(assigned_users=request.user)
    
    if filter_param == 'completed':
        tasks = base_queryset.filter(status=True)
    elif filter_param == 'pending':
        tasks = base_queryset.filter(status=False)
    else:
        tasks = base_queryset
    
    context = {
        'tasks': tasks,
        'filter': filter_param,
        'is_admin': request.user.is_staff
    }
    return render(request, 'tasks/task_list.html', context)



class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')