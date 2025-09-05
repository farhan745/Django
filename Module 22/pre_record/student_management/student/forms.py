from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
class StudentForm(forms.ModelForm):
    class Meta:   
        model = models.Student
        exclude = ['user','updated_by']  # user field ke exclude korlam, karon eta automatically set hobe view theke

        # Field er label change
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'password': 'Password',
            'checkbox': 'Agree to Terms',
            'photo': 'Upload Photo',
        }

        # Field er help text add
        help_texts = {
            'name': 'Enter your full name.',
            'email': 'Enter a valid email address.',
            'phone': 'Enter your phone number.',
            'password': 'Choose a strong password.',
            'checkbox': 'You must agree to the terms to proceed.',
            'photo': 'Upload a recent photo.',
        }
        widgets = {
            'password': forms.PasswordInput(),  # Password field er jonno
            'checkbox': forms.CheckboxInput(),  # Checkbox er jonno
        }
        
        
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {

            'username': 'User Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {

            'username': 'Enter your desired username.',
            'email': 'Enter a valid email address.',
            'password1': 'Choose a strong password.',
            'password2': 'Confirm your password.',
        }
        widgets = {
            'password1': forms.PasswordInput(),  # Password field er jonno
            'password2': forms.PasswordInput(),  # Password field er jonno
        }


class EmailLoginForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email Address",
        required=True,   # খালি রাখা যাবে না
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your registered email',  # শুধু placeholder
        })
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',  
        })
    )

    class Meta:
        model = models.Student
        fields = ['email', 'password']
       
        