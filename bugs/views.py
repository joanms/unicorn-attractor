from django.shortcuts import render, redirect, reverse, get_object_or_404
from bugs.forms import BugReportForm
from .models import Bug
from django.contrib.auth.decorators import login_required


@login_required()
def report_bug(request):
    """
    Renders a form for reporting bugs
    """
    if request.method == 'POST':
        bug_form = BugReportForm(request.POST or None)
        if bug_form.is_valid():
            bug_form.submitter = request.user
            bug = bug_form.save()
            return redirect(bug_detail, bug.pk)
    else:
        bug_form = BugReportForm()
    return render(request, 'report_bug.html', {'bug_form': bug_form})
    

def bug_detail(request, pk):
    """
    Create a view that returns a singleBug object based on the 
    bug ID (pk) and render it to the 'bug_detail.html' template
    or return a 404 error if the bug is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, "bug_detail.html", {'bug': bug})


    
def view_bugs(request):
    """
    Displays a table listing all reported bugs
    """
    bugs = Bug.objects.all()
    return render(request, 'view_bugs.html', {'bugs': bugs})