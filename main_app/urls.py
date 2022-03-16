from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boroughs/', views.borough_index, name='borough_index'),
    path('boroughs/<int:borough_id>/', views.borough_detail, name='borough_detail'),
    path('neighborhoods/', views.neighborhood_index, name='neighborhood_index'),
    path('neighborhoods/<int:neighborhood_id>/', views.neighborhood_detail, name='neighborhood_detail'),
    path('points_of_interest/', views.point_of_interest_index, name='point_of_interest_index'),
    path('points_of_interest/<str:point_of_interest_id>/', views.point_of_interest_detail, name='point_of_interest_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('point_of_interest/<int:point_of_interest_id>/add_review/<int:user_id>', views.add_review, name='add_review'),
]
