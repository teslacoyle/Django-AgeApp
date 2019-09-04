from django.http import HttpResponse

def welcome(request):
    return HttpResponse("ur a bich")