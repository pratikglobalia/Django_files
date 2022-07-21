import email
from django.shortcuts import render
from .forms import Userregistration
from .models import User

# Create your views here.
def userdata(request):
    if request.method == 'POST':
        fm = Userregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']           
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = Userregistration()   
    return render(request,'regdata.html',{'form': fm})
