from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def borough_index(request):
    boroughs = Borough.objects.all()
    return render(request, 'borough_index.html', { 'boroughs': boroughs })

def neighborhood_index(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'neighborhood_index.html', { 'neighborhoods' : neighborhoods })

def point_of_interest_index(request):
    entertainment = Entertainment.objects.all()
    accommodation = Accommodation.objects.all()
    sightseeing = SightSeeing.objects.all()
    food = Food.objects.all()
    art_culture = Art_Culture.objects.all()
    return render(request, 'interest_index.html', {
        'entertainment': entertainment,
        'accomodation': accommodation,
        'sightseeing': sightseeing,
        'food': food,
        'art_culture': art_culture
    })
