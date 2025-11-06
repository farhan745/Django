from django import forms
from .models import Post, Category, Tag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content',
            'category': 'Category',
            'tags': 'Tags',
        }
        help_texts = {
            'title': 'Enter the title of the post.',
            'content': 'Write the content of the post here.',
            'category': 'Select a category for the post.',
            'tags': 'Select relevant tags for the post.',
        }



        
