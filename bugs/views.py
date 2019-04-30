from django.shortcuts import render, redirect, reverse
from bugs.forms import BugReportForm
from .models import Bug
from django.contrib.auth.decorators import login_required


@login_required()
def report_bug(request):
    """Renders a form for reporting bugs"""
    bug_form = BugReportForm(request.POST or None)
    if bug_form.is_valid():
        bug_form.submitter = request.user
        bug_form.save()
    context = {
        'bug_form': bug_form
    }
    return render(request, 'report_bug.html', context)
    
    
def view_bugs(request):
    """Displays a table listing all reported bugs"""
    bugs = Bug.objects.all()
    return render(request, 'view_bugs.html', {'bugs': bugs})