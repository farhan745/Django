from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
class UserRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-input mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
    }))
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input mt-1, block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                                    }))
    password2 = forms.CharField(label='Confirm Password', 
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input mt-1, block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                                                                }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'profile_picture': 'Profile Picture',
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
            'profile_picture': None,
        }
class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']  # completed bad
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'category': 'Category',
            'priority': 'Priority',
            'status': 'Status',
            'due_date': 'Due Date',
        }
        help_texts = {
            'title': None,
            'description': None,
            'category': None,
            'priority': None,
            'status': None,
            'due_date': None,
        }