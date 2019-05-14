from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.forms import FeatureReportForm, CommentForm
from .models import Feature, Comment, Upvote
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def report_feature(request):
    """
    Renders a form for reporting features and saves a feature with the currently 
    logged-in user as its submitter if a valid form is submitted.
    """
    if request.method == 'POST':
        feature_form = FeatureReportForm(request.POST)
        if feature_form.is_valid():
            feature = feature_form.save(commit=False)
            feature.submitter = request.user
            feature.save()
            request.user.profile.features_submitted += 1
            request.user.profile.save()
            return redirect(view_features)
    else:
        feature_form = FeatureReportForm()
    return render(request, 'request_feature.html', {'feature_form': feature_form})

    
def view_features(request):
    """
    Displays a table listing all reported features
    """
    features = Feature.objects.all()
    return render(request, 'view_features.html', {'features': features})
    

def feature_detail(request, pk):
    """
    Displays a single feature or returns a 404 error if the feature is not found, 
    and displays comments on the feature
    """
    feature = get_object_or_404(Feature, pk=pk)
    comments = Comment.objects.filter(feature=feature)
    return render(request, "feature_detail.html", {'feature': feature, 'comments': comments})
    

@login_required()
def comment(request, pk):
    """
    Renders a form for commenting on features and saves a feature with the currently 
    logged-in user as the commenter if a valid form is submitted.
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.feature = feature
            comment.save()
            return redirect(feature_detail, feature.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'feature_comment.html', {'feature': feature, 'comment_form': comment_form})
    

# The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
@login_required()
def upvote(request, feature_id):
    """
    Allows users to upvote features they didn't submit themselves 
    and haven't already upvoted
    """
    feature = Feature.objects.get(pk=feature_id)
    comments = Comment.objects.filter(feature=feature)
    if request.user == feature.submitter:
        messages.error(request, "You can't upvote a feature that you submitted.")
    elif Upvote.objects.filter(user=request.user, feature=feature):
        messages.error(request, "You have already upvoted this feature.")
    else:
        feature.upvotes += 1
        feature.save()
        upvote = Upvote.objects.create(user=request.user, feature=feature)

    return render(request, "feature_detail.html", {'feature': feature, 'comments': comments})