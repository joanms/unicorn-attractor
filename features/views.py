from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.forms import FeatureReportForm, FeatureCommentForm
from .models import Feature, FeatureComment, FeatureUpvote
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def request_feature(request):
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
            return redirect(all_features)
    else:
        feature_form = FeatureReportForm()
    return render(request, 'request_feature.html', {'feature_form': feature_form})

    
def all_features(request):
    """
    Displays a table listing all reported features
    """
    features = Feature.objects.all()
    return render(request, 'all_features.html', {'features': features})
    

def feature_details(request, pk):
    """
    Displays a single feature or returns a 404 error if the feature is not found, 
    and displays comments on the feature
    """
    feature = get_object_or_404(Feature, pk=pk)
    comments = FeatureComment.objects.filter(feature=feature)
    return render(request, "feature_details.html", {'feature': feature, 'comments': comments})
    

@login_required()
def feature_comment(request, pk):
    """
    Renders a form for commenting on features and saves a feature with the currently 
    logged-in user as the commenter if a valid form is submitted.
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == 'POST':
        comment_form = FeatureCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.feature = feature
            comment.save()
            return redirect(feature_details, feature.pk)
    else:
        comment_form = FeatureCommentForm()
    return render(request, 'feature_comment.html', {'feature': feature, 'comment_form': comment_form})