from django.db import models
from django.utils import timezone
from accounts.models import Profile

class Feature(models.Model):
    """
    A single feature
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(Profile, null=False)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title