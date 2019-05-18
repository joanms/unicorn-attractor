# This code was copied and adapted for this project from the e-commerce mini project

from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Ensures that the cart contents are 
    available when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    feature_count = 0
    
    for id, price in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += price
        cart_items.append({'id': id, 'price': price, 'feature': feature})
    
    return {'cart_items': cart_items, 'total': total, 'feature_count': feature_count}