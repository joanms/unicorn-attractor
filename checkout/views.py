# This code was copied and adapted for this project from the e-commerce mini project

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature, FeatureUpvote
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """
    Check validity of order form and payment, 
    and make payment if they are valid
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid():
            print("Order form is valid")
        else:
            print("Order form is NOT valid")
        if payment_form.is_valid():
            print("Payment form is valid")
        else:
            print("Payment form is NOT valid")

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * feature.price
                order_line_item = OrderLineItem(
                    order=order,
                    feature=feature,
                    quantity=quantity
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
                # The quantity of upvotes purchased and amount paid are added to the feature object
                feature.upvotes += quantity
                feature.amount_paid += total
                feature.save()
                # An upvote object is created with the transaction details
                upvote = FeatureUpvote.objects.create(user=request.user, feature=feature, amount_paid=total)
                request.session['cart'] = {}
                return redirect(reverse('list_features'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})