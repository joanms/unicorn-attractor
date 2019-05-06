from django.shortcuts import render, redirect, reverse, get_object_or_404
from bugs.forms import BugReportForm, CommentForm
from .models import Bug, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def report_bug(request):
    """
    Renders a form for reporting bugs
    """
    if request.method == 'POST':
        bug_form = BugReportForm(request.POST or None)
        if bug_form.is_valid():
            bug = bug_form.save(commit=False)
            bug.submitter = request.user
            bug.save()
            request.user.profile.bugs_submitted += 1
            request.user.profile.save()
            return redirect(view_bugs)
    else:
        bug_form = BugReportForm()
    return render(request, 'report_bug.html', {'bug_form': bug_form})
    

def bug_detail(request, pk):
    """
    Create a view that returns a single Bug object based on the 
    bug ID (pk) and render it to the 'bug_detail.html' template
    or return a 404 error if the bug is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    comments = Comment.objects.filter(bug_id=bug)
    return render(request, "bug_detail.html", {'bug': bug, 'comments': comments})


    
def view_bugs(request):
    """
    Displays a table listing all reported bugs
    """
    bugs = Bug.objects.all()
    return render(request, 'view_bugs.html', {'bugs': bugs})
    

def upvote(request, bug_id):
    """
    Allows users to upvote bugs they didn't submit themselves 
    and haven't already upvoted
    """
    bug = Bug.objects.get(pk=bug_id)
    if request.user == bug.submitter:
        messages.error(request, "You can't upvote a bug that you submitted.")
        
    # I need an elif statement here checking whether the user has already upvoted 
    # and, if so, telling them that they can't upvote again.
    
    else:
        bug.upvotes += 1
        bug.save()

    bugs = Bug.objects.all()
    return redirect('/bugs/view_bugs/')
    

def comment(request, pk):
    """
    Renders a form for commenting on bugs
    """
    bug = get_object_or_404(Bug, pk=pk)
    comments = Comment.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.save()
            return render(request, 'bug_detail.html', {'bug': bug, 'comments': comments})
    else:
        comment_form = CommentForm()
    return render(request, 'bug_comment.html', {'comment_form': comment_form, 'bug': bug})