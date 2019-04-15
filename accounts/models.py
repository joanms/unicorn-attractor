from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    A user's profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bugs_submitted = models.IntegerField(default=0)
    features_submitted = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.user.username