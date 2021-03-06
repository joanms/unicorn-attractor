""" This code was copied and adapted for this project from the e-commerce mini project"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """
    Check validity of order form and payment, and make 
    payment and update database if they are valid
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            """
            If the order form and payment are valid, the 
            order object is created and saved in the database
            """
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.upvoter = request.user
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, price in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += price
                order_line_item = OrderLineItem(
                    order=order,
                    feature=feature,
                    price=price
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                """
                The quantities of upvotes purchased and amounts paid are added to 
                the Features table in the database. This code is not from the 
                e-commerce mini-project. I adapted it from Marcin Mrugacz's project: 
                https://github.com/Migacz85/django_app/blob/master/checkout/views.py. 
                """
                upvote_list = []
                for id, price in cart.items():
                    upvote_list.append(id)
                for id in upvote_list:
                    feature = get_object_or_404(Feature, id=id)
                    feature.upvotes += 1
                    feature.amount_paid += price
                    feature.save()
                request.session['cart'] = {}    
                return redirect(reverse('all_features'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})