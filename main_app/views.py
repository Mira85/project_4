from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def borough_index(request):
    boroughs = Borough.objects.all()
    return render(request, 'borough/borough_index.html', { 'boroughs': boroughs })

def borough_detail(request, borough_id):
    neighborhoods = Neighborhood.objects.filter(borough=borough_id)
    borough = Borough.objects.get(id=borough_id)
    return render(request, 'borough/borough_detail.html', { 
        'neighborhoods' : neighborhoods,
        'borough': borough
    })

def neighborhood_index(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'neighborhood/neighborhood_index.html', { 'neighborhoods' : neighborhoods })

def neighborhood_detail(request, neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    entertainment = Entertainment.objects.get(neighborhood=neighborhood_id)
    accommodation = Accommodation.objects.get(neighborhood=neighborhood_id)
    art_culture = Art_Culture.objects.get(neighborhood=neighborhood_id)
    sightseeing = SightSeeing.objects.get(neighborhood=neighborhood_id)
    nature = Nature.objects.get(neighborhood=neighborhood_id)
    return render(request, 'neighborhood/neighborhood_detail.html', {
        'neighborhood': neighborhood,
        'entertainment' : entertainment,
        'accommodation' : accommodation,
        'art_culture' : art_culture,
        'sightseeing' : sightseeing,
        'nature' : nature
    })

def point_of_interest_index(request):
    entertainment = Entertainment.objects.all()
    accommodation = Accommodation.objects.all()
    sightseeing = SightSeeing.objects.all()
    food = Food.objects.all()
    art_culture = Art_Culture.objects.all()
    return render(request, 'interest/interest_index.html', {
        'entertainment': entertainment,
        'accomodation': accommodation,
        'sightseeing': sightseeing,
        'food': food,
        'art_culture': art_culture
    })
