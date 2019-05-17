# This code was copied and adapted for this project from the e-commerce mini project

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_one(request, id):
    """
    Increment quantity of an item in the cart. 
    Code by Marcin Mrugacz.
    """
    cart = request.session.get('cart', {})
    if cart[id] > 0:
        cart[id] = cart[id] + 1
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_one(request, id):
    """
    Decrement quantity of an item in the cart. 
    Code by Marcin Mrugacz.
    """
    cart = request.session.get('cart', {})
    if cart[id] > 1:
        cart[id] = cart[id] - 1

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
