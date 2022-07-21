from django.shortcuts import render, HttpResponse
from custom import signals

# Create your views here.
def home(request):
    signals.notification.send(sender=None, request=request, user=['pratik', 'patel'])
    return HttpResponse('Home page')