from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Editer')
            user.groups.add(group)
            messages.success(request,'Data save successfully')
    else:
        fm = Signupform()
    return render(request,'reg.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logging Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request,'userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')



def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return HttpResponseRedirect('/login/')


def user_dashbord(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html', {'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

