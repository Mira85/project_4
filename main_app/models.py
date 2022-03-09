from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Borough(models.Model):
    name = models.CharField(max_length=175)
    image = models.CharField(max_length = 220)

class Neighborhood(models.Model):
    name = models.CharField(max_length=175)
    description = models.TextField(max_length=275)
    image = models.CharField(max_length=250)
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE)

class Entertainment(models.Model):
    name = models.CharField(max_length=275)
    type_of = models.CharField(max_length=150)
    price = models.IntegerField(
        default= 0,
        validators= [
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    description = models.TextField(max_length=275)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class SightSeeing(models.Model):
    name = models.CharField(max_length=275)
    price = models.IntegerField(
        default= 0,
        validators= [
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    description = models.TextField(max_length=275)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class Nature(models.Model):
    name = models.CharField(max_length=250)
    season = models.CharField(max_length=20)
    image = models.CharField(max_length=275)
    description = models.TextField(max_length=375)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=250)
    cuisine = models.CharField(max_length=250)
    price = models.IntegerField(
        default= 0,
        validators= [
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    image = models.CharField(max_length=350)
    description = models.TextField(max_length=350)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class Art_Culture(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(
        default= 0,
        validators= [
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    image = models.CharField(max_length=350)
    description = models.TextField(max_length=350)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    
class Accommodation(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(
        default= 0,
        validators= [
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    type_of = models.CharField(max_length=150)
    image = models.CharField(max_length=350)
    description = models.TextField(max_length=350)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)



