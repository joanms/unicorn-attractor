from django import forms
from .models import Bug, Comment


class BugReportForm(forms.ModelForm):
    """
    Form for users to report bugs
    """
    class Meta:
        model = Bug
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