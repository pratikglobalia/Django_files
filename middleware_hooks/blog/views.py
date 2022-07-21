from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('i am view')
    return HttpResponse('Home page')

def excp(request):
    print('i am exception view')
    10/0
    return HttpResponse('Exception page')

def user_info(request):
    print('user info')
    context = {'name':'pratik'}
    return TemplateResponse(request,'user.html',context)
    