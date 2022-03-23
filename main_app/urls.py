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
    path('point_of_interest/<str:point_of_interest_id>/add_review/<int:user_id>/', views.add_review, name='add_review'),
    path('point_of_interest/<str:point_of_interest_id>/update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('point_of_interest/<str:point_of_interest_id>/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('user/<int:user_id>/my_list/', views.user_list, name="user_list"),
    path('user/<int:user_id>/my_list/add_itinerary/', views.add_itinerary, name='add_itinerary'),
    path('user/<int:user_id>/<int:itinerary_id>/add_to_itinerary/<str:point_of_interest_id>/<str:point_of_interest_name>/', views.add_to_itinerary, name='add_to_itinerary'),
    path('point_of_interest/search', views.search, name='search')
]
