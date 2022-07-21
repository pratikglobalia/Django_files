import email
from unicodedata import name
from django.shortcuts import render
from .forms import Userregistration
from .models import Student


# Create your views here.
def userdata(request):
    if request.method == 'POST':
        fm = Userregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']           
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # reg = Student(name=nm, email=em, password=pw)
            # reg.save()
            # reg = Student(id=5, name=nm, email=em, password=pw)
            # reg.save()
            reg = Student(id=5)
            reg.delete()
            
    else:
        fm = Userregistration()   
    return render(request,'reg.html',{'form': fm})
