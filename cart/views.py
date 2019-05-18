# This code was copied and adapted for this project from the e-commerce mini project

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from features.models import Feature


@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Set the price of a feature to add to the cart"""
    price = int(request.POST.get('price'))
    cart = request.session.get('cart', {})
    feature = get_object_or_404(Feature, id=id)
    feature_id = str(feature.id)

    if feature_id in cart:
        messages.error(request, "That feature is already in your cart. To change the price, please click or tap the buttons next to the feature price.")
    else:    
        cart[id] = cart.get(id, price)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_one(request, id):
    """
    Increment price of an item in the cart. 
    Adpated from code by Marcin Mrugacz.
    """
    cart = request.session.get('cart', {})
    cart[id] = cart[id] + 1
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_one(request, id):
    """
    Decrement price of an item in the cart. 
    Adapted from code by Marcin Mrugacz.
    """
    cart = request.session.get('cart', {})
    if cart[id] > 5:
        cart[id] = cart[id] - 1
    else:
        messages.error(request, "The minimum fee is €5.")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
