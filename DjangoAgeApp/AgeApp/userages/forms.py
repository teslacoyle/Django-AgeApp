from django.forms import ModelForm
from .models import AgeProfile

class AgeProfileForm(ModelForm):
    class Meta:
        model = AgeProfile
        exclude = ('user') 