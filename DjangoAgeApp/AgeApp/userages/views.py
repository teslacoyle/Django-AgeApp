from django.shortcuts import render
from django.http import HttpResponse
from .models import AgeProfile

# Create your views here.
def home(request):
    if not request.user:
        return HttpResponse('ur not logged in dud')
    profile = AgeProfile.objects.filter(
            user = request.user
        ).first()
    # TODO this is not permanent - error or something
    if not profile:
        profile = AgeProfile.objects.first()
    profiles = AgeProfile.objects.all().order_by('age')
    return render(request, 'userages/home.html',
                  {'age' : profile.age, 'name' : profile.user.username})
