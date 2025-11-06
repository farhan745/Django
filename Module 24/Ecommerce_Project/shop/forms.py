from django import forms
from .models import CartItem, Order, Product, Category
from django.forms import ModelForm
from django.contrib.auth.models import User
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Category Name'})
        }
        labels = {
            'name': 'Category Name'
        }
        help_texts = {
            'name': 'Enter the name of the category.'
        }
        
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
            'image': forms.ClearableFileInput(),
        }
        labels = {
            'category': 'Category',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'stock': 'Stock',
            'image': 'Image',
            
        }
        help_texts = {
            'price': 'Enter the price in USD.',
            'stock': 'Enter the available stock quantity.',
            'image': 'Upload an image of the product.',
            
        }
        