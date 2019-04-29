from django import forms
from .models import Bug


class BugReportForm(forms.ModelForm):
    """Form for users to report bugs"""
    class Meta:
        model = Bug
        fields = ['title', 'description']
    title = forms.CharField()
    description = forms.Textarea()