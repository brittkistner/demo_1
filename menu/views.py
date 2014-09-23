import random
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from demo1 import settings
from menu.forms import EmailUserCreationForm, FoodQuantityForm
from menu.models import Menu, Food, ShoppingCart, Restaurant, Order, ShoppingCartFoodQuantity, OrderFoodQuantity

import yelp


yelp_api = yelp.Api(consumer_key="z4wowXpPjMIOQ7YboOBy6g",
                    consumer_secret="MZUvylqq0OVkhJXaZOwwoyQBTFM",
                    access_token_key="Ca9XgVmPC14COPKKzMvrTZi-3xr8C7Fr",
                    access_token_secret="1N1asF0HVFK3Cf9m0E4rww7ch58")

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>You joined at {}.  I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("search")

    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

# PROFILE #
@login_required()
def profile(request):
    customer = request.user
    data = {"customer": customer}
    return render(request, 'profile.html', data)

# @login_required()
# def edit_profile(request):


# SEARCH #
@login_required()
def search(request):
    return render(request,"search.html")

def search_lat_long(request, coordinates):
    match = re.search(r'=([^&]*)&[^=]*=(.*)$',coordinates)
    my_lat = float(match.group(1))
    my_longi = float(match.group(2))
    restaurant_list= Restaurant.objects.filter(lat__range=(my_lat-.02, my_lat +.02)).filter(longi__range=(my_longi-.02, my_longi+.02))
    return restaurants(request,restaurant_list)

#RESTAURANT PICK #
@login_required()
def restaurants(request, restaurant_list):
    data = {'restaurants': restaurant_list}
    return render(request, 'restaurants.html', data)

def restaurant_info(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    business=yelp_api.GetBusiness(restaurant.yelp_id)
    deal=business.deals

    address=business.location.address[0]
    review1 = random.choice(business.reviews)
    # review2 = random.choice(business.reviews)


    data = {'business': business,
            "restaurant":restaurant,
            "address": address,
            "deal":deal,
            "review1": review1,
            # "review2": review2,
    }
    return render(request, 'restaurant_info.html', data)


def check_shopping_cart_by_restaurant_and_customer(restaurant, customer):
    shopping_cart_list = restaurant.shopping_carts.values('id')
    if not shopping_cart_list:
        return False
    else:
        customer_shopping_carts = customer.shopping_carts.filter(pk__in=shopping_cart_list)
        if not customer_shopping_carts:
            return False
        else:
            return True

def get_shopping_cart(restaurant, customer):
    shopping_cart_list = restaurant.shopping_carts.values('id')
    return customer.shopping_carts.filter(pk__in=shopping_cart_list)[0]

#RESTAURANT MENU #
@login_required()
def get_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    customer = request.user
    menu = Menu.objects.get(restaurant=restaurant_id)
    foods = {}
    for food in menu.foods.all():
        form = FoodQuantityForm({'food': food.id, 'quantity': 0})
        foods[food] = form

    types = {}
    for food in menu.foods.all():
        if food.tag in types:
            types[food.tag].append(food)
        else:
            types[food.tag] = [food]

    data = {"customer": customer, "foods": foods, "types": types}
    if check_shopping_cart_by_restaurant_and_customer(restaurant, customer) == True:
        shopping_cart = get_shopping_cart(restaurant, customer)
        data['shopping_cart'] = shopping_cart
    else:
        shopping_cart = ShoppingCart(customer=customer,restaurant=restaurant).save()
        data['shopping_cart'] = shopping_cart

    if request.method == 'POST':
        form=FoodQuantityForm(request.POST)
        quantity = int(form['quantity'].value())
        food_id = int(form['food'].value())

        food_quantity = ShoppingCartFoodQuantity.objects.filter(shopping_cart=shopping_cart.id, food=food_id)

        if not food_quantity:
            food_quantity = ShoppingCartFoodQuantity(food=Food.objects.get(pk=food_id), shopping_cart=shopping_cart, quantity=quantity)
            food_quantity.save()
        else:
            food_quantity = food_quantity[0]
            food_quantity.quantity += quantity
            food_quantity.save()

    return render(request, 'restaurant_menu.html', data)

#Checkout#
@login_required()
def checkout(request,cart_id):
    cart = ShoppingCart.objects.get(pk=cart_id)
    food_quantities = cart.food_quantities.all()
    restaurant = cart.restaurant
    customer = request.user
    order = Order(customer=customer,restaurant=restaurant)
    order.save()
    for food_quantity in food_quantities:
        # food_id = food_quantity.food.id
        food = food_quantity.food
        quantity = food_quantity.quantity
        order_food_quantity = OrderFoodQuantity(food=food, quantity=quantity, order=order)
        order_food_quantity.save()
        food_quantity.delete()
    cart.delete()

    data={
        'order':order,
        'restaurant':restaurant,
    }
    return render(request, 'checkout.html', data)

#Purchase Complete#
@login_required()
def purchase_complete(request):
    customer = request.user
    data = {"customer": customer}
    return render(request, 'confirm_purchase.html', data)
