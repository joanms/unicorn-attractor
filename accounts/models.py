from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    A user's profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bugs_submitted = models.IntegerField(default=0)
    features_submitted = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __str__(self):
        return self.user.username