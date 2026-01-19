from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404 , render
# BASE DE DATOS
from .models import Project, Task

# Create your views here.

def index(request):
    title = 'Welcome to Django Course!!'
    return render(request,'index.html', {
        'title':title
    })

def logout(request):
    username='Hola Pollo'
    return render(request,'about.html', {
        'username':username
    })

def hello(request, username):
    return HttpResponse(f"<h2> Hellos Word {username}<h2>")

def projects (request):
    # projects =list(Project.objects.values())
    # return JsonResponse(projects,safe=False)
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects':projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse(f"Task : {task.title}")
    return render(request, 'tasks.html')