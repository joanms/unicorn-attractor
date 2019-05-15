# This code was copied and adapted for this project from the e-commerce mini project

from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]