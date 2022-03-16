from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm
from decouple import config
import requests
# Create your views here.

API_KEY = config('API_KEY')
NEIGHBORHOOD_BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="

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
    payload={}
    headers = {}
    place_list = []
    
    # API URLS
    tourist_attraction_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=tourist_attraction&key={API_KEY}"
    response = requests.get(tourist_attraction_url, headers=headers, data=payload)
    neighborhood_tourist_attractions = response.json()['results']
    for result in neighborhood_tourist_attractions:
        places = {
            "name": result['name'],
            "address": result['formatted_address'],
            "interest_category": result['types'],
            "rating": result['rating'],
            "id": result['place_id'],
        }
        place_list.append(places)

    example = neighborhood_tourist_attractions[0]
    return render(request, 'neighborhood/neighborhood_fetch.html', {
        'neighborhood': neighborhood,
        'points_of_interest': place_list,
    } )

def point_of_interest_index(request):
    points_of_interest = Point_Of_Interest.objects.all()
    return render(request, 'interest/interest_index.html', { 'points_of_interest' : points_of_interest })

def point_of_interest_detail(request, point_of_interest_id):
    fetch_detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={point_of_interest_id}&key={API_KEY}"
    payload={}
    headers = {}
    response = requests.get(fetch_detail_url, headers=headers, data=payload)
    point_of_interest = response.json()['result']
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={point_of_interest['photos'][0]['photo_reference']}&key={API_KEY}"
    place_details = {
        'address': point_of_interest['formatted_address'],
        # 'phone_number': point_of_interest['formatted_phone_number'],
        'name': point_of_interest['name'],
        # 'open_hours': point_of_interest['opening_hours'],
        'photo': photo_url,
        'id': point_of_interest['place_id'],
        # 'rating': point_of_interest['rating'],
        # 'reviews': point_of_interest['reviews'],   
    }
    
    return render(request, 'interest/interest_fetch.html', {
        'point_of_interest': place_details
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid sign up - please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

def add_review(request, point_of_interest_id, user_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit = False)
        new_review.point_of_interest_id = point_of_interest_id
        new_review.user_id = user_id
        new_review.save()
    return redirect('point_of_interest_detail', point_of_interest_id = point_of_interest_id)
    