from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #ADMIN#
    url(r'^admin/', include(admin.site.urls)),
    #LOGIN AND REGISTER
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'wanderful.views.register', name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # PASSWORD RESET
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    #HOME#
    url(r'^$', 'menu.views.home', name='home'),
    #Restaurants Around User#
    url(r'^pick/$', 'menu.views.pick_restaurant', name='pick_restaurant'),
    #Restaurant Menu#
    url(r'^restaurant/(?P<menu_id>\w+)/$','menu.views.restaurant_menu', name='restaurant_menu'),





)
