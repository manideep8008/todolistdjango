from django.shortcuts import HttpResponse,render
from todo.models import Task

def home(request):
    taskscom=Task.objects.filter(is_completed=False).order_by('-updatedAt')
    completed=Task.objects.filter(is_completed=True)
    
    context={
        'taskscom':taskscom,
        "completed":completed
    }
    # tasksinc=Task.objects.filter(is_completed=True)
    # context={
    #     "tasksinc":tasksinc
    # }
    return render(request,"home.html",context)