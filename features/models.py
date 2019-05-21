from django.db import models
from django.utils import timezone
from accounts.models import User


class Feature(models.Model):
    """
    A single feature
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateField(auto_now_add=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    status = models.TextField(default="To do")

    def __str__(self):
        return self.title
        

class FeatureComment(models.Model):
    """
    A comment on a feature
    """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_commenter')
    text = models.TextField()

    def __str__(self):
        return "Comment on {0} by {1} on {3}".format(
            self.feature, self.commenter, self.comment_date)        
