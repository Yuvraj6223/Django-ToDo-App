from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    print(request.POST)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_task_text = request.POST.get('task')
        task.task = new_task_text
        task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')