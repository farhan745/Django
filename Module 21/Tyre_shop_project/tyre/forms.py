from django import forms
from .models import Tyre
class TyreForm(forms.ModelForm):
    class Meta:
        model = Tyre
        fields = ['tyre_name', 'tyre_size', 'description','company', 'image']
        labels = {
            'tyre_name': 'Tyre Name',
            'tyre_size': 'Tyre Size',
            'company': 'Company',
            'image': 'Tyre Image',
        }
        help_texts = {
            'tyre_name': 'Enter tyre name',
            'tyre_size': 'Enter tyre size',
            'company': 'Enter company name',
            'image': 'Upload an image of the tyre',
        }
        widgets = {
            'tyre_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tyre_size': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }