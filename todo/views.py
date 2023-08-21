from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Task
# Create your views here.
def addTask(request):

    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('/')

def mark_as_done(request,pk):
    task= get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('/')

def undo(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('/')

def editTask(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('/')
    else:
        context={
            'get_task':get_task
        }
        return render(request,'editTask.html',context)


def deleteTask(request,pk):
    delte_task = get_object_or_404(Task, pk=pk)
    delte_task.delete()
    return redirect('/')

