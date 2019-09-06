from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class AgeProfile(models.Model):
#     email = models.CharField(max_length=50)
#     age = models.IntegerField()

# Probably go with this one-- deleting and such. 
# Just make sure it isn't unsafe to use a direct realationship to an internal auth class.
class AgeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='age_profile', primary_key=True)
    age = models.IntegerField()

    def __str__(self):
        return '{0}, age {1}'.format(self.user.username, self.age)