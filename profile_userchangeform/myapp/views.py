from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Signupform, EditUserProfile, EditAdminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=request.user)
            else:
                fm = EditUserProfile(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated !!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfile(instance=request.user)
                users = None
        return render(request,'profile.html', {'name': request.user, 'form':fm, 'users':users})
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
    

def  user_detaile(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfile(instance=pi)
        return render(request,'userdetails.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')