from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    name = models.CharField(max_length=30)
    # img = models.ImageField(upload_to='customer_images', blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)

class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    lat = models.FloatField(null=True)
    longi = models.FloatField(null=True)
    img = models.ImageField(upload_to='restaurant_images', blank=True, null=True)
    yelp_id = models.CharField(max_length=60,null=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    tag = models.ForeignKey(Tag, related_name='foods')

    def __unicode__(self):
        return self.name


class Order(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='orders',default=0)
    status = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, related_name='orders', default=0)

    def total(self):
        food_quantities = self.food_quantities.all()
        total = 0
        for food_quantity in food_quantities:
            total += food_quantity.food.price * food_quantity.quantity

        return total

class OrderFoodQuantity(models.Model):
    food = models.ForeignKey(Food, related_name='order_quantities')
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, related_name='food_quantities')
    def __unicode__(self):
        return u"{}".format(self.food)

class Menu(models.Model):
    name = models.CharField(max_length=30)
    foods = models.ManyToManyField(Food, related_name='menus')
    restaurant = models.ForeignKey(Restaurant, related_name='menus')

    def __unicode__(self):
        return self.name

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, related_name='shopping_carts')
    restaurant = models.ForeignKey(Restaurant, related_name='shopping_carts')

    def total(self):
        food_quantities = self.food_quantities.all()
        subtotal = 0
        for food_quantity in food_quantities:
            subtotal += food_quantity.food.price * food_quantity.quantity

        return subtotal

class ShoppingCartFoodQuantity(models.Model):
    food = models.ForeignKey(Food, related_name='shopping_cart_quantities')
    quantity = models.IntegerField(default=0)
    shopping_cart = models.ForeignKey(ShoppingCart, related_name='food_quantities')

    def __unicode__(self):
        return u"{}".format(self.food)

