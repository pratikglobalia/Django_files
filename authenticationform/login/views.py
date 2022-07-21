from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
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
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return HttpResponseRedirect('/login/')



def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Change Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
    
    

def user_changepass_withoutpass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Change Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request,'changepass1.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')