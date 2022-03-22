from django.forms import ModelForm
from .models import Review
from django import forms 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('ratings', 'description')
        widgets = {
            'ratings' : forms.NumberInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }
       