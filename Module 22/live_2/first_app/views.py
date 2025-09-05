from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout # rename here
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Home view
@login_required(login_url='login')  # ensure user is logged in to access home
def home(request):         # login page এ পাঠাবে
    return render(request, 'index.html')   # login থাকলে home page দেখাবে

# Signup view
def signup(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')  # redirect should match view name
    context = {'form': form}
    return render(request, 'signup.html', context)

# Login view
def login_view(request):  # rename view function
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user_obj = User.objects.get(email=email)  # email দিয়ে user খোঁজা
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)  # use renamed auth_login
                    request.session['user_id'] = user.id
                    request.session['email'] = user.email
                    messages.success(request, 'Login successful')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid password')
            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)  # use renamed auth_logout
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # redirect should match view name

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)# Important! jodi password change kore tahole session valid thakbe taile abar login korte hobe na
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
        
            