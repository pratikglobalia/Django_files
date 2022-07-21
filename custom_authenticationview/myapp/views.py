from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'myapp/home.html'

class DashBoard(TemplateView):
    template_name = 'myapp/dashboard.html'
    
class Login(LoginView):
    template_name = 'myapp/login.html'
    
class Logout(LogoutView):
    template_name = 'myapp/logout.html'
    
class PassWordChange(PasswordChangeView):
    template_name = 'myapp/changepass.html'
    success_url = '/changepassdone/'
    
class PassWordChangeDone(PasswordChangeDoneView):
    template_name = 'myapp/changepassdone.html'