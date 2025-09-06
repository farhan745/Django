from django.shortcuts import render,redirect,get_object_or_404
from .models import Task,Profile
from .forms import TaskForm,RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def TaskList(request):
    
    search_input = request.GET.get('search-area') or ''
    if request.user.is_superuser:
        # Superuser সব task দেখতে পারবে
        task = Task.objects.all()
    else:
        # Normal user শুধু তার নিজের task দেখতে পারবে
        task = Task.objects.filter(user=request.user)
    if search_input:
        task = task.filter(title__icontains=search_input)
    
    
    return render(request, 'todo_app_list.html', {'tasks': task, 'search_input': search_input})
@login_required
def TaskCreate(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    return render(request, 'todo_app_create.html', {'form': form})
@login_required
def TaskUpdate(request,id):
    
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app_create.html', {'form': form, 'task': task})
@login_required
def TaskDelete(request,id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'todo_app_delete.html', {'task': task})
@login_required
def TaskDetail(request,id):
    task = get_object_or_404(Task, id=id, user=request.user)
    return render(request, 'todo_app_detail.html', {'task': task})


def RegisterUser(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # save profile info
            bio = form.cleaned_data.get('bio')
            image = form.cleaned_data.get('image')
            Profile.objects.create(user=user, bio=bio, profile=image)
            # log the user in
            login(request, user)
            return redirect('task-list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form,'signup': True})

#Email diye login

def LoginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('task-list')
                else:
                    messages.error(request, 'Invalid email or password.')
            except:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,'signup': True})
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile.html', {'user': user})
