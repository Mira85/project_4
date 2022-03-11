from django.contrib import admin
from .models import Borough, Neighborhood, Point_Of_Interest, Review

admin.site.register(Borough)
admin.site.register(Neighborhood)
admin.site.register(Point_Of_Interest)
admin.site.register(Review)

