from django.shortcuts import HttpResponse,render
from todo.models import Task

def home(request):
    taskscom=Task.objects.filter(is_completed=False).order_by('-updatedAt')
    context={
        'taskscom':taskscom
    }
    # tasksinc=Task.objects.filter(is_completed=True)
    # context={
    #     "tasksinc":tasksinc
    # }
    return render(request,"home.html",context)