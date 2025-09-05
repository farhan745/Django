from . import models
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'published': 'Published',
        }
        help_texts = {
            'title': 'Enter the title of the post.',
            'content': 'Enter the content of the post.',
            'published': 'Check if the post is published.',
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'author': 'Author',
            'text': 'Comment',
        }
        help_texts = {
            'author': 'Enter your name.',
            'text': 'Enter your comment.',
        }
        