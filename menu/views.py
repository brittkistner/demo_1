from django.contrib.auth import authenticate, login
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from demo1 import settings
from menu.forms import EmailUserCreationForm
from menu.models import Menu, Food, ShoppingCart


def home(request):
    return render (request, 'home.html')

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
            return redirect("profile")

    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def pick_restaurant(request):
    data = {#pull in time of day so a menu can be chosen (breakfast, lunch, or dinner)

    }
    return render(request, 'pick.html', data)

def restaurant_menu(request,menu_id):
    menu = Menu.objects.get(menu_id)           #FEATURE: get all menus since it could be more than one
    customer = request.user
    foods = Food.objects.filter(menus=menu_id)
    shopping_cart = ShoppingCart.objects.create(customer.id,) #FINISH
    data = {
        "menu" : menu,
        "customer" : customer,
        "foods": foods,
        "shopping_cart": shopping_cart,
    }
    return render(request, 'restaurant_menu.html', data)



# @login_required
# def profile(request):
#     traveller = request.user
#     data = {"traveller" : traveller}
#     return render(request, 'profile.html', data)


