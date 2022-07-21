
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms  

class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
