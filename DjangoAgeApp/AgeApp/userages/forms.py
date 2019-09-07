from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import AgeProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']

class AgeProfileForm(ModelForm):
    class Meta:
        model = AgeProfile
        exclude = ['user']