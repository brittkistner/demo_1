from django.contrib import admin
from menu.models import Restaurant, Food, Tag, Order, Menu, Customer

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Menu)



