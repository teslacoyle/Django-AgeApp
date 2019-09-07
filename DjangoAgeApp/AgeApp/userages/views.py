from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import AgeProfile
from collections import Counter
import string
import timeit

# Create your views here.
@login_required
def home(request):
    profile = AgeProfile.objects.filter(
            user = request.user
        ).first()
    ages = AgeProfile.objects.order_by('age').values_list('age', flat=True)
    min_age = ages[0]
    max_age = ages[ages.count()-1]
    counts = dict(Counter(ages))

    return render(request, 'userages/home.html',
                  {'age' : profile.age, 
                   'name' : profile.user.username, 
                   'axisLabels' : ','.join([str(x) for x in range(min_age, max_age+1)]),
                   'axisValues' : ','.join([str(counts[i]) if i in counts.keys() else "0" for i in range(min_age, max_age+1)]),
                   'colorValues' : ','.join(["'rgba(255, 0, 0, 0.4)'" if i == profile.age else "'rgba(230, 230, 230, 0.4)'" for i in range(min_age, max_age+1)]),
                   'counts' : counts }) 


