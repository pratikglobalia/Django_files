from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    10/0
    return HttpResponse('hello')