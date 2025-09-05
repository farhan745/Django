from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    tasks = models.Task.objects.all()
    return render(request,'task_app/home.html',{'tasks':tasks})
def delete_task(request,id):
    task = models.Task.objects.get(id=id)
    task.delete()
    return redirect('home')
def task_details(request,id):
    task = models.Task.objects.get(id=id)
    return render(request,'task_app/task_details.html',{'task':task})