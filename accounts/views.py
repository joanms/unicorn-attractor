"""This was copied and adapted for this project from the Authentication and Authorisation unit of the course."""

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug, BugUpvote
from features.models import Feature
from checkout.models import OrderLineItem


@login_required
def logout(request):
    """Log the user out and empty the shopping cart"""
    auth.logout(request)
    request.session['cart'] = {}
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                """
                If the user was redirected to the login page when they tried to 
                do something that requires login, the following 3 lines of code 
                redirect them back to the page they were on once they log in. I 
                added the code to the code copied from the course material.
                """
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                return render(request, 'profile.html', {"profile": user})
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    bug_reports = Bug.objects.filter(submitter=user)
    feature_requests = Feature.objects.filter(submitter=user)
    bug_upvotes = BugUpvote.objects.filter(user=user)
    feature_upvotes = OrderLineItem.objects.filter(order__upvoter=user)
    return render(request, 'profile.html', {"profile": user, "bug_reports": bug_reports, 
    "feature_requests": feature_requests, "bug_upvotes": bug_upvotes, "feature_upvotes": feature_upvotes})