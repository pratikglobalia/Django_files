from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django_fee(request):
    return HttpResponse(10000)


def python_fees(request):
    return HttpResponse(15000)
    