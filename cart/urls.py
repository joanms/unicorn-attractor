""" 
This code was copied and adapted for this project from the e-commerce mini project.
The code for adding and subtracting is based on code by Marcin Mrugacz.
"""

from django.conf.urls import url
from .views import view_cart, add_to_cart, add_one, subtract_one, delete_item

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^add_one/(?P<id>\d+)/$', add_one, name='add_one'),
    url(r'^subtract_one/(?P<id>\d+)/$', subtract_one, name='subtract_one'),
    url(r'^delete_item/(?P<id>\d+)/$', delete_item, name='delete_item'),
]