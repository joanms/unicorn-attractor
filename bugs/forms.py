from django import forms
from .models import Bug, BugComment


class BugReportForm(forms.ModelForm):
    """
    Form for users to report bugs
    """
    class Meta:
        model = Bug
        fields = ['title', 'description']
    title = forms.CharField()
    description = forms.Textarea()
    

class BugCommentForm(forms.ModelForm):
    """
    Form for users to comment on bugs
    """
    class Meta:
        model = BugComment
        fields = ['text']
    text = forms.Textarea()