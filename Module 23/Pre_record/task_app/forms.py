from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'complete': 'Completed',
        }
        help_texts = {
            'title': 'Enter the title of the task.',
            'description': 'Provide a detailed description of the task.',
            'complete': 'Check if the task is completed.',
        }
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','bio', 'image']
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'image': 'Profile Image',
        }
#todo: Email diye
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password = forms.CharField(
        label='Password',
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    