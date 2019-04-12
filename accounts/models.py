from django.db import models
from django.utils import timezone

class User(models.Model):
    """
    A user's profile
    """
    username = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=70,blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    bugs_submitted = models.IntegerField(default=0)
    features_submitted = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.title