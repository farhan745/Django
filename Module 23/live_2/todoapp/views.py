from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login, authenticate
from . import models
# Create your views here.
def hello(request):
    return HttpResponse("<h1 class='text-4xl font-light text-blue-600'>Hello, world. You're at the todoapp index.</h1>")
@login_required
def hello_protected(request):
    return render(request, 'protected.html')
def index(request):
    return HttpResponse("<h1 class='text-4xl font-light text-blue-600'>Hello, world. You're at the todoapp index.</h1>")
def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            picture = form.cleaned_data.get('profile_picture')
            models.Profile.objects.create(user=user, picture=picture)
            login(request, user)
            return redirect('hello_protected')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def task_list(request):
    tasks = models.Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})
@login_required
def create_task(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = forms.TaskForm()
    return render(request, 'create_task.html', {'form': form})
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(models.Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = forms.TaskForm(instance=task)
    return render(request, 'create_task.html', {'form': form, 'task': task, 'edit': True})
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(models.Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
    return redirect('task_list')
    