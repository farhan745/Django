from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:   
        model = models.Student
        fields = '__all__'

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