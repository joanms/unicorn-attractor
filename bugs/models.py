from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Bug(models.Model):
    """
    A single bug
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateField(auto_now_add=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    
    STATUS_CHOICES = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='To do'
    )

    def __str__(self):
        return self.title
        

class BugUpvote(models.Model):
    """
    An upvote on a bug
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.bug.title        
        

class BugComment(models.Model):
    """
    A comment on a bug
    """
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return "{0}: {1}".format(
            self.bug, self.text)        
