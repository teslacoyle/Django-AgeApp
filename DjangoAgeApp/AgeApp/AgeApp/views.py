from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('age_home')
    else:
        return redirect('userages_login')