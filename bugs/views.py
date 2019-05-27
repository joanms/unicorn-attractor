from django.shortcuts import render, redirect, reverse, get_object_or_404
from bugs.forms import BugReportForm, BugCommentForm
from .models import Bug, BugComment, BugUpvote
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def report_bug(request):
    """
    Renders a form for reporting bugs and saves a bug with the currently 
    logged-in user as its submitter if a valid form is submitted.
    """
    if request.method == 'POST':
        bug_form = BugReportForm(request.POST)
        if bug_form.is_valid():
            bug = bug_form.save(commit=False)
            bug.submitter = request.user
            bug.save()
            request.user.profile.bugs_submitted += 1
            request.user.profile.save()
            return redirect(all_bugs)
    else:
        bug_form = BugReportForm()
    return render(request, 'report_bug.html', {'bug_form': bug_form})

    
def all_bugs(request):
    """
    Displays a table listing all reported bugs
    """
    bugs = Bug.objects.all()
    return render(request, 'all_bugs.html', {'bugs': bugs})
    

def bug_details(request, pk):
    """
    Displays a single bug or returns a 404 error if the bug is not found, 
    and displays comments on the bug
    """
    bug = get_object_or_404(Bug, pk=pk)
    user = request.user
    comments = BugComment.objects.filter(bug=bug)
    if user.is_authenticated():
        """Checks whether the logged-in user has already upvoted the bug"""
        user_upvoted = BugUpvote.objects.filter(user=request.user, bug=bug)
        return render(request, "bug_details.html", {'bug': bug, 'comments': comments, 'user_upvoted': user_upvoted})
    return render(request, "bug_details.html", {'bug': bug, 'comments': comments})    
    

@login_required()
def bug_comment(request, pk):
    """
    Renders a form for commenting on bugs and saves a bug with the currently 
    logged-in user as the commenter if a valid form is submitted.
    """
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == 'POST':
        comment_form = BugCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.bug = bug
            comment.save()
            return redirect(bug_details, bug.pk)
    else:
        comment_form = BugCommentForm()
    return render(request, 'bug_comment.html', {'bug': bug, 'comment_form': comment_form})
    

# The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
@login_required()
def upvote_bug(request, bug_id):
    """
    Allows users to upvote bugs they haven't already upvoted
    """
    bug = Bug.objects.get(pk=bug_id)
    comments = BugComment.objects.filter(bug=bug)
    if BugUpvote.objects.filter(user=request.user, bug=bug):
        messages.error(request, "You have already upvoted this bug.")
    else:
        bug.upvotes += 1
        bug.save()
        upvote = BugUpvote.objects.create(user=request.user, bug=bug)

    return render(request, "bug_details.html", {'bug': bug, 'comments': comments})