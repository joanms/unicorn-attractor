from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from bugs.models import Bug
from features.models import Feature


class Profile(models.Model):
    """
    A user's profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bugs_submitted = models.IntegerField(default=0)
    features_submitted = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
        
        
"""The following code is from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone"""

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile. """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the user profile after creation"""
    instance.profile.save()