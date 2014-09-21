from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    name = models.CharField(max_length=30)
    # Do you need an abstract user?  Probably not, could change back to auth user to set permissions

    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    lat = models.FloatField(null=True)
    longi = models.FloatField(null=True)
    img = models.ImageField(upload_to='restaurant_images', blank=True, null=True)

    def __unicode__(self):
        return self.name

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

class Order(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    customers = models.ManyToManyField(Customer, related_name='orders')
    status = models.BooleanField(default=True)
    #Use NullBooleanField()??
    food_quantity = models.IntegerField(default=0)
    foods = models.ManyToManyField(Food, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, related_name='orders', default=0)


class Menu(models.Model):
    name = models.CharField(max_length=30)
    foods = models.ManyToManyField(Food, related_name='menus')
    restaurant = models.ForeignKey(Restaurant, related_name='menus')

    def __unicode__(self):
        return self.name

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, related_name='shopping_carts')
    restaurant = models.ForeignKey(Restaurant, related_name='shopping_carts')
    foods = models.ManyToManyField(Food, related_name='shopping_carts', blank=True, null=True)
    food_quantity = models.IntegerField(default=0)



#CREATE ANOTHER APP FOR STAFF(could possible be a regular user)
