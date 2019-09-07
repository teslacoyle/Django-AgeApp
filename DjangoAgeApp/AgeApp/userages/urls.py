from django.urls import path
from .views import home, register

urlpatterns = [
        path('home', home, name='age_home'),
        path('register', register, name = 'userages_register')
    ]
