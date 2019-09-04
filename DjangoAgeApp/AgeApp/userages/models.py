from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class AgeProfile(models.Model):
#     email = models.CharField(max_length=50)
#     age = models.IntegerField()

# Probably go with this one-- deleting and such. 
# Just make sure it isn't unsafe to use a direct realationship to an internal auth class.
class AgeProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='age_profile')
    age = models.IntegerField()