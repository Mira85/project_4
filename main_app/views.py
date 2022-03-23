from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm, ItineraryForm
from decouple import config
import requests
import urllib.parse

from django.contrib.auth.decorators import login_required
# Create your views here.

API_KEY = config('API_KEY')
NEIGHBORHOOD_BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
PHOTO_BASE_URL = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference="

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
    result_list = []
    place_list = []
    
    # API URLS
    # Tourist Attractions
    tourist_attraction_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=tourist_attraction&key={API_KEY}"
    response = requests.get(tourist_attraction_url, headers=headers, data=payload)
    neighborhood_tourist_attractions = response.json()['results']
    result_list.append(neighborhood_tourist_attractions)

    # Restaurants
    restaurant_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=restaurant&key={API_KEY}"
    response = requests.get(restaurant_url, headers=headers, data=payload)
    neighborhood_restaurants = response.json()['results']
    result_list.append(neighborhood_restaurants)
    
    # Night Clubs
    club_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=night_club&key={API_KEY}"
    response = requests.get(club_url, headers=headers, data=payload)
    neighborhood_clubs = response.json()['results']
    result_list.append(neighborhood_clubs)

    #Lodging
    lodging_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=lodging&key={API_KEY}"
    response = requests.get(lodging_url, headers=headers, data=payload)
    neighborhood_lodging = response.json()['results']
    result_list.append(neighborhood_lodging)

    # Clothing_Store
    clothing_store_url = f"{NEIGHBORHOOD_BASE_URL}{neighborhood.name}&type=clothing_store&key={API_KEY}"
    response = requests.get(clothing_store_url, headers=headers, data=payload)
    neighborhood_clothing_stores = response.json()['results']
    result_list.append(neighborhood_clothing_stores)


    for genre in result_list:
        for result in genre:
            if ['photos'][0] in result:
                photo_url = f"{PHOTO_BASE_URL}{result['photos'][0]['photo_reference']}&key={API_KEY}"
                place = {
                    "name": result['name'],
                    "address": result['formatted_address'],
                    "interest_category": result['types'],
                    "rating": result['rating'],
                    "id": result['place_id'],
                    'photo': photo_url
                }
                place_list.append(place)
            else:
                place = {
                    "name": result['name'],
                    "address": result['formatted_address'],
                    "interest_category": result['types'],
                    "rating": result['rating'],
                    "id": result['place_id'],
                    'photo': "https://t3.ftcdn.net/jpg/04/34/72/82/360_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg"
                }
                place_list.append(place)

        tourist_attractions = []
        for place in place_list: 
            if 'tourist_attraction' in place['interest_category']:
                tourist_attractions.append(place)
        tourist_range = tourist_attractions[0:3]
        tourist_rest = tourist_attractions[3:]
        
        restaurants = []
        for place in place_list: 
            if 'restaurant' in place['interest_category']:
                restaurants.append(place)
        restaurant_range = restaurants[0:3]
        restaurant_rest = restaurants[3:]
        
        places_to_stay = []
        for place in place_list: 
            if 'lodging' in place['interest_category']:
                places_to_stay.append(place)
        places_to_stay_range = places_to_stay[0:3]
        places_to_stay_rest = places_to_stay[3:]
        
        clubs = []
        for place in place_list: 
            if 'night_club' in place['interest_category']:
                clubs.append(place)
        clubs_range = clubs[0:3]
        clubs_rest = clubs[3:]
        
        parks = []
        for place in place_list: 
            if 'park' in place['interest_category']:
                parks.append(place)
        parks_range = parks[0:3]
        parks_rest = parks[3:]
        
        shops = []
        for place in place_list: 
            if 'clothing_store' in place['interest_category']:
                shops.append(place)
        shops_range = shops[0:3]
        shops_rest = shops[3:]
        
    return render(request, 'neighborhood/neighborhood_fetch.html', {
        'neighborhood': neighborhood,
        'points_of_interest': place_list,
        'tourist_range': tourist_range,
        'tourist_rest' : tourist_rest,
        'restaurant_range': restaurant_range,
        'restaurant_rest' : restaurant_range,
        'places_to_stay_range': places_to_stay_range,
        'places_to_stay_rest': places_to_stay_rest,
        'clubs_range' : clubs_range,
        'clubs_rest' : clubs_rest,
        'parks_range' : parks_range,
        'parks_rest' : parks_rest,
        'shops_range' : shops_range,
        'shops_rest' : shops_rest
    } )

def point_of_interest_index(request):
    return render(request, 'interest/interest_index.html')


def point_of_interest_detail(request, point_of_interest_id):
    fetch_detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={point_of_interest_id}&key={API_KEY}"
    payload={}
    headers = {}
    response = requests.get(fetch_detail_url, headers=headers, data=payload)
    point_of_interest = response.json()['result']
    itineraries = Itinerary.objects.filter(user__exact=request.user.id)
    photo_url = f"{PHOTO_BASE_URL}{point_of_interest['photos'][0]['photo_reference']}&key={API_KEY}"
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

    review_form = ReviewForm()
    itinerary_form = ItineraryForm()

    all_reviews = Review.objects.filter(point_of_interest_id = point_of_interest_id )
    user_review = all_reviews.filter(user__exact=request.user.id)
    other_review = all_reviews.exclude(user__exact=request.user.id)
    review_form=ReviewForm()
    if user_review:
        review_form = ReviewForm(instance = user_review.first())

    return render(request, 'interest/interest_fetch.html', {
        'point_of_interest': place_details,
        'review_form': review_form,
        'user_review': user_review,
        'other_review': other_review,
        'all_reviews': all_reviews,
        'itinerary_form': itinerary_form,
        'itineraries': itineraries
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

@login_required
def add_review(request, point_of_interest_id, user_id):
    form = ReviewForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_review = form.save(commit = False)
            new_review.point_of_interest_id = point_of_interest_id
            new_review.user_id = user_id
            new_review.save()
        return redirect('point_of_interest_detail', point_of_interest_id = point_of_interest_id)

@login_required
def update_review(request, point_of_interest_id, review_id):
    data = Review.objects.get(id=review_id)
   
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('point_of_interest_detail', point_of_interest_id = point_of_interest_id)
   

@login_required
def delete_review(request, point_of_interest_id, review_id):
    data = Review.objects.get(id=review_id)

    if request.method == "POST":
        data.delete()
        return redirect('point_of_interest_detail', point_of_interest_id = point_of_interest_id)

@login_required
def user_list(request, user_id):
    itinerary_form = ItineraryForm()
    user = User.objects.get(id=user_id)
    itineraries = Itinerary.objects.filter(user=user_id)
    return render(request, 'user/user_list.html', {
        'itinerary_form': itinerary_form,
        'user': user,
        'itineraries': itineraries
    })

@login_required
def add_itinerary(request, user_id):
    form = ItineraryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_itinerary = form.save(commit = False)
            new_itinerary.user_id = user_id
            new_itinerary.save()
        return redirect('user_list', user_id = user_id)

@login_required
def add_to_itinerary(request, user_id, itinerary_id, point_of_interest_id, point_of_interest_name, ):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    point_of_interest = f"{point_of_interest_name} {point_of_interest_id}"
    itinerary.points_of_interest_id.append(point_of_interest_id)
    itinerary.points_of_interest_name.append(point_of_interest_name)
    itinerary.points_of_interest.append(point_of_interest)
    itinerary.save()
    return redirect('point_of_interest_detail', point_of_interest_id = point_of_interest_id)

@login_required
def delete_from_itinerary(request, user_id, itinerary_id,point_of_interest, name, id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == "POST":
        for interest in itinerary.points_of_interest:
            if interest == point_of_interest:
                interest.delete()
        for name in itinerary.points_of_interest:
            if interest == point_of_interest:
                interest.delete()
        for interest in itinerary.points_of_interest:
            if interest == point_of_interest:
                interest.delete()

        return redirect('user_list', user_id)


@login_required
def delete_itinerary(request, user_id, itinerary_id ):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == "POST":
        itinerary.delete()
        return redirect('user_list', user_id)

def search(request):
    payload={}
    headers = {}
    if request.method == "POST":
        searched = request.POST['searched']
        url_search_term = urllib.parse.quote(" " + searched)
        searched_url = f"{NEIGHBORHOOD_BASE_URL}newyorkcity{url_search_term}&key={API_KEY}"
        response = requests.get(searched_url, headers=headers, data=payload)
        place_id = response.json()['results'][0]['place_id']
        return redirect('point_of_interest_detail', point_of_interest_id = place_id)
    else:
         return render(request, 'interest/interest_index.html')
