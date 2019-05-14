from django import forms
from .models import Feature, FeatureComment


class FeatureReportForm(forms.ModelForm):
    """
    Form for users to report features
    """
    class Meta:
        model = Feature
        fields = ['title', 'description']
    title = forms.CharField()
    description = forms.Textarea()
    

class FeatureCommentForm(forms.ModelForm):
    """
    Form for users to comment on bugs
    """
    class Meta:
        model = FeatureComment
        fields = ['text']
    text = forms.Textarea()