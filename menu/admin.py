from django.contrib import admin
from menu.models import Restaurant, Food, Tag, Order, Menu, Customer, ShoppingCart, ShoppingCartFoodQuantity, \
    OrderFoodQuantity

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Tag)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartFoodQuantity)
admin.site.register(OrderFoodQuantity)




