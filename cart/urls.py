# This code was copied and adapted for this project from the e-commerce mini project

from django.conf.urls import url
from .views import view_cart, add_to_cart, add_one, remove_one

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^add_one/(?P<id>\d+)/$', add_one, name='add_one'),
    url(r'^remove_one/(?P<id>\d+)/$', remove_one, name='remove_one'),
]