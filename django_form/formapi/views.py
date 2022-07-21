from django.shortcuts import render
from .form import StudentRegistration 

# Create your views here.
def showstudata(request):
    stud = StudentRegistration()
    return render(request,'userreg.html',{'form':stud})