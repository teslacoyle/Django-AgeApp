from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import AgeProfile
from .forms import RegisterForm, AgeProfileForm
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

@require_http_methods(["GET", "POST"])
def register(request):
    if(request.method == "POST"):
        user_form = RegisterForm(request.POST)
        age_form = AgeProfileForm(request.POST)
        if user_form.is_valid() and age_form.is_valid():
            user_profile = user_form.save(commit = False)
            user_profile.username = user_profile.email
            user_form.save()
            age_profile = age_form.save(commit = False)
            age_profile.user = user_profile
            age_profile.save()

            # login
            auth_user= authenticate(username=user_form.cleaned_data['email'], password = user_form.cleaned_data['password1'])
            if auth_user is not None:
                login(request, auth_user)
                return redirect('age_home')
            else:
                return redirect('userages_login')
    else:
        register_form = RegisterForm()
        age_form = AgeProfileForm()
        return render(request, "userages/register.html", {'reg_form': register_form, 'age_form': age_form})
