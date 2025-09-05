from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'student_class', 'email', 'photo']
        labels = {
                'name': 'Full Name',
                'roll': 'Roll Number',
                'student_class': 'Class',
                'email': 'Email Address',
                'photo': 'Profile Photo',
            }
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
                'roll': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
                'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class (e.g. 10th Grade)'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
                'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }