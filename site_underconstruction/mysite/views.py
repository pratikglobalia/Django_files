from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('WelCome!!...This is our site Home page')

def about(request):
    return HttpResponse('WelCome!!...This is our site About page')
    