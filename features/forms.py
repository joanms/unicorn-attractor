from django import forms
from .models import Feature, Comment


class FeatureReportForm(forms.ModelForm):
    """
    Form for users to report features
    """
    class Meta:
        model = Feature
        fields = ['title', 'description']
    title = forms.CharField()
    description = forms.Textarea()
    

class CommentForm(forms.ModelForm):
    """
    Form for users to comment on bugs
    """
    class Meta:
        model = Comment
        fields = ['text']
    text = forms.Textarea()