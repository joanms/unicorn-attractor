""" This code was copied from the e-commerce mini project"""

from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]