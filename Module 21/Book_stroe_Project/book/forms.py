from django import forms
from django.forms import ModelForm
from .models import BookStore

class BookForm(ModelForm):
    class Meta:
        model = BookStore
        fields = ['id', 'book_name', 'author', 'category']
        labels = {
            'id': 'Book ID',
            'book_name': 'Book Name',
            'author': 'Author Name',
            'category': 'Category',
        }
        help_texts = {
            'id': 'Enter Book ID',
            'book_name': 'Enter Book Name',
            'author': 'Enter Author Name',
            'category': 'Select Category',
        }
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book ID'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Name'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author Name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
