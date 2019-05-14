from django.db import models
from django.utils import timezone
from accounts.models import User


class Feature(models.Model):
    """
    A single feature
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        

class FeatureUpvote(models.Model):
    """
    An upvote on a feature
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_upvoter')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2, null=True)
        

class FeatureComment(models.Model):
    """
    A comment on a feature
    """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_commenter')
    text = models.TextField()

    def __str__(self):
        return self.text        