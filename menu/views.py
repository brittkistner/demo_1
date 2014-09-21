import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from demo1 import settings
from menu.forms import EmailUserCreationForm, FoodCountForm
from menu.models import Menu, Food, ShoppingCart, Restaurant, Order


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
    # restaurants = []  #are you passing in restaurant objects??  If so, then just pass directly to data
    # for restaurant_id in restaurant_id_list:
    #     restaurants.append(Restaurant.objects.get(pk=restaurant_id))
    data = {'restaurants': restaurant_list}
    return render(request, 'restaurants.html', data)

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
    return customer.shopping_carts.filter(pk__in=shopping_cart_list)[0]  #polish up

#RESTAURANT MENU #
@login_required()
def get_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    customer = request.user
    menu = Menu.objects.get(restaurant=restaurant_id)
    foods = Food.objects.filter(menus=menu.id)
    data = {"customer": customer, "foods":foods, "menu":menu}
    if check_shopping_cart_by_restaurant_and_customer(restaurant, customer) == True:
        shopping_cart = get_shopping_cart(restaurant, customer)
        data['shopping_cart'] = shopping_cart
    else:
        shopping_cart = ShoppingCart(customer=customer,restaurant=restaurant).save()
        data['shopping_cart'] = shopping_cart

    #FORM
    # if request.method == 'POST':
    #     form=FoodCountForm(request.POST)
    #     if form.is_valid():
    #         quantity = form.cleaned_data['quantity']
    #         food = form.cleaned_data['food']
    #create food_quantity (how to identity food id???)
                # food_quantity = FoodAndCount(food=food, quantity=quantity)
                # shopping_cart = Current instance of shopping_cart
                # shopping_cart.food_quantity.add(food_quantity)
#can add or delete foods
    # else:

        return render(request, 'restaurant_menu.html', data)

#Checkout#

# @login_required()
# def checkout(request,cart_id):
#     cart = ShoppingCart.objects.get(pk=cart_id)
#     food_quantities = cart.food_quantity.all()
#     restaurant = Restaurant.objects.get(shopping_carts__pk=cart_id)
#     customer = request.user
#     order = Order(customers=customer,restaurant=restaurant)
#     order.save()
#     for food_quantity in food_quantities:
#         order.food_quantity.add(food_quantity)
#     cart.delete()
#
#     data={
#         'order':order,
#         'restaurant':restaurant,
#         'customer':customer,
#     }
#     return render(request, 'checkout.html', data)

#Purchase Complete#
@login_required()
def purchase_complete(request):
    customer = request.user
    data = {"customer": customer}
    return render(request, 'confirm_purchase.html', data)

