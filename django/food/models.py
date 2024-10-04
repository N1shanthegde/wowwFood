from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.CharField(max_length=500, default='Not specified')
    calories = models.CharField(max_length=50, null=True, blank=True)
    pimg = models.URLField()
    
    
    
class Burger(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=6, decimal_places=2)
    priceL = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.CharField(max_length=500, default='Not specified')
    calories = models.CharField(max_length=50, null=True, blank=True)
    bimg = models.URLField()
    
from django.db import models

class Momos(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Default value added
    # priceL = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Default value added
    material = models.CharField(max_length=500, default='Not specified')
    calories = models.CharField(max_length=50, null=True, blank=True)
    mimg = models.URLField()




    
class Sandwich(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.CharField(max_length=500, default='Not specified')
    calories = models.CharField(max_length=50, null=True, blank=True)
    simg = models.URLField()

    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=60)
    bill = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add = True, blank=True)
    note = models.TextField(blank=True, null=True)


class Item(models.Model):
    order =  models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=60)