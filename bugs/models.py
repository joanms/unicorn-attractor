from django.db import models
from django.utils import timezone

class Bug(models.Model):
    """
    A single bug
    """
    title = models.CharField(max_length=50)
    date_submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.CharField(max_length=50)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title