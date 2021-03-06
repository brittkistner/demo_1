from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from demo1 import settings

urlpatterns = patterns('',
    #ADMIN#
    url(r'^admin/', include(admin.site.urls)),
    #LOGIN AND REGISTER
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'menu.views.register', name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    # PASSWORD RESET
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    #PROFILE#
    url(r'^profile/$', 'menu.views.profile', name='profile'),
    # url(r'^/edit/$', 'menu.views.edit_profile', name='edit_profile'),
    #Search#
    url(r'^search/$', 'menu.views.search', name='search'),
    url(r'^search/(?P<coordinates>.*)/$', 'menu.views.search_lat_long', name='search_lat_long'),
    #Restaurant#
    url(r'^restaurants/(?P<restaurant_list>\w+)/$', 'menu.views.restaurants', name='restaurants'),

    url(r'^restaurant/(?P<restaurant_id>\w+)/$', 'menu.views.restaurant_info', name='restaurant_info'),
    #Menu#
    url(r'^menu/(?P<restaurant_id>\w+)/$', 'menu.views.get_menu', name='get_menu'),
    #Cart#
    #Checkout#
    url(r'^checkout/(?P<cart_id>\w+)/$', 'menu.views.checkout', name='checkout'),
    #Purchase#
    url(r'^purchase_complete/$', 'menu.views.purchase_complete', name='purchase_complete'),


    #HOME#
    # url(r'^$', 'menu.views.home', name='home')

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
