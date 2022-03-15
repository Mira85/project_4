from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Borough(models.Model):
    name = models.CharField(max_length=175)
    image = models.CharField(max_length = 220)
    
    def __str__(self):
        return f'{self.name}, NY'

class Neighborhood(models.Model):
    name = models.CharField(max_length=175)
    description = models.TextField(max_length=275)
    image = models.CharField(max_length=250)
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.borough.name}'

class Point_Of_Interest(models.Model):
    name = models.CharField(max_length=250)
    interest_category = models.CharField(max_length=100)
    type_of = models.CharField(max_length=100, default='')
    price = models.IntegerField(
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(4)
        ])
    image = models.CharField(max_length = 300)
    description = models.TextField(max_length = 300)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)  


class Review(models.Model):
    ratings = models.IntegerField(
        default = 0,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ])
    description = models.TextField(max_length = 300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point_of_interest = models.ForeignKey(Point_Of_Interest, on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.point_of_interest} has {self.ratings} rating'



