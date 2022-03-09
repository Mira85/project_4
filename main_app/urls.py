from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boroughs/', views.borough_index, name='borough_index'),
    path('neighborhoods/', views.neighborhood_index, name='neighborhood_index'),
    path('points_of_interest/', views.point_of_interest_index, name='point_of_interest_index'),
]