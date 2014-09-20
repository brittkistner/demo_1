from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    name = models.CharField(max_length=30)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    #FINISH (Yelp)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    customers = models.ManyToManyField(Customer, related_name='orders')
    status = models.BooleanField(default=True)
    #Use NullBooleanField()??
    food_quantity = models.IntegerField()
    foods = models.ManyToManyField(Food, related_name='orders')


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    tags = models.ManyToManyField(Tag, related_name='foods')

    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=30)
    foods = models.ManyToManyField(Food, related_name='menus')
    restaurant = models.ForeignKey(Restaurant, related_name='menus')

    def __unicode__(self):
        return self.name

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, related_name='shopping_cart')
    foods = models.ManyToManyField(Food, related_name='shopping_carts')
    food_quantity = models.IntegerField(default=0)
#     foreign key for restaurant

#CREATE ANOTHER APP FOR STAFF(could possible be a regular user)
