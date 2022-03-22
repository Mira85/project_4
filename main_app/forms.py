from django.forms import ModelForm
from .models import Review, Itinerary

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('ratings', 'description')

class ItineraryForm(ModelForm):
    class Meta: 
        model = Itinerary
        fields = ['name']