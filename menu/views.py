import re
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from demo1 import settings
from menu.forms import EmailUserCreationForm
from menu.models import Menu, Food, ShoppingCart, Restaurant


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
# @login_required
def profile(request):
    customer = request.user
    data = {"customer": customer}
    return render(request, 'profile.html', data)

# SEARCH #
def search(request):
    return render(request,"search.html")

def search_lat_long(request, coordinates):
    match = re.search(r'=([^&]*)&[^=]*=(.*)$',coordinates)
    my_lat = float(match.group(1))
    my_longi = float(match.group(2))
    restaurant_list= Restaurant.objects.filter(lat__range=(my_lat-.02, my_lat +.02)).filter(longi__range=(my_longi-.02, my_longi+.02))
    return restaurants(request,restaurant_list)

#RESTAURANT PICK #
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
        customer_shopping_carts = customer.shopping_cart.filter(pk__in=shopping_cart_list)
        if not customer_shopping_carts:
            return False
        else:
            return True

def get_shopping_cart(restaurant, customer):
    shopping_cart_list = restaurant.shopping_carts.values('id')
    return customer.shopping_cart.filter(pk__in=shopping_cart_list)[0]  #polish up

def get_menu(request, restaurant_id):
    # if request.method == 'POST':
    #     form = EmailUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         text_content = 'Thank you for signing up for our website, {}'.format(user.username)
    #         html_content = '<h2>Thanks {} {} for signing up!</h2> <div>You joined at {}.  I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
    #         msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
    #         msg.attach_alternative(html_content, "text/html")
    #         msg.send()
    #         new_user = authenticate(username=request.POST['username'],
    #                                 password=request.POST['password1'])
    #         login(request, new_user)
    #         return redirect("search")
    #
    # else:
        menu = Menu.objects.get(restaurant=restaurant_id)
        customer = request.user
        foods = Food.objects.filter(menus=menu.id)
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        if get_shopping_cart_by_restaurant_and_customer(restaurant, customer) == True:
            shopping_cart = get_shopping_cart(restaurant, customer)
        else:
            shopping_cart = ShoppingCart(customer=customer,restaurant=restaurant).save()
        data = {
            "menu": menu,
            "customer": customer,
            "foods": foods,
            "shopping_cart": shopping_cart,
            # form = EmailUserCreationForm(),
        }

        return render(request, 'restaurant_menu.html', data)


# def cart(request, ) (POST REQUEST)
# in the url/ checkout?cartid
# Cart = get(cart_id)
# may need to hash out cart stuff in order to make the order
# create the order
# delete the cart
#have a button on the page to say (purchase)


#def checkout(request,) (POST REQUEST)

#def order(request, ) (Post and send to staff)




