from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_oq6ujj'
    )

    # Return the profile in reverse order
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}s profile'

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

'''
This will listen for a user being created and 
will call the create profile function
'''
post_save.connect(create_profile, sender=User)