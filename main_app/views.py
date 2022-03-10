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
    points_of_interest = Point_Of_Interest.objects.filter(neighborhood=neighborhood_id)
    return render(request, 'neighborhood/neighborhood_detail.html', {
        'neighborhood': neighborhood,
        'points_of_interest': points_of_interest
    })

def point_of_interest_index(request):
    points_of_interest = Point_Of_Interest.objects.all()
    return render(request, 'interest/interest_index.html', { 'points_of_interest' : points_of_interest })

def point_of_interest_detail(request, point_of_interest_id):
    point_of_interest = Point_Of_Interest.objects.get(id=point_of_interest_id)
    return render(request, 'interest/interest_detail.html', { 'point_of_interest' : point_of_interest})