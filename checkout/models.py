""" This code was copied from the e-commerce mini project except where noted. """

from django.db import models
from accounts.models import User
from features.models import Feature

class Order(models.Model):
    """I added upvoter to this model"""
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    upvoter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    """
    I modified this model from the course material to include the price instead 
    of the quantity because the quantity is always 1 and the user sets the price
    """
    order = models.ForeignKey(Order, null=False)
    feature = models.ForeignKey(Feature, null=False)
    price = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return "{0}: {1}".format(
            self.feature.title, self.price)