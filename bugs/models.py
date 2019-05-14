from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bug(models.Model):
    """
    A single bug
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    status = models.TextField(default="To do")

    def __str__(self):
        return self.title
        

class BugUpvote(models.Model):
    """
    An upvote on a bug
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, null=True)
        

class BugComment(models.Model):
    """
    A comment on a bug
    """
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text