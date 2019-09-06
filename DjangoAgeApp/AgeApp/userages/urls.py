from django.urls import path
from .views import home

urlpatterns = [
        path('home', home, name='age_home')
    ]
