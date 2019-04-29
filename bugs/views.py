from django.shortcuts import render, redirect, reverse
from bugs.forms import BugReportForm

# Create your views here.
def report_bug(request):
    bug_form = BugReportForm(request.POST or None)
    if bug_form.is_valid():
        bug_form.save()
        
    context = {
        'bug_form': bug_form
    }    
        
    return render(request, 'report_bug.html', context)