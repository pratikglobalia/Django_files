from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def stuinfo(request):
    fm = StudentRegistration()
    return render(request,'userinfo.html',{'data':fm})