from django.forms import ModelForm
from .models import Review, Itinerary
from django import forms 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('ratings', 'description')
        widgets = {
            'ratings' : forms.NumberInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class ItineraryForm(ModelForm):
    class Meta: 
        model = Itinerary
        fields = ['name']