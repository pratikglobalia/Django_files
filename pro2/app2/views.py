from django.shortcuts import render
from datetime import datetime

# Create your views here.
def django_fees(request):
    d = datetime.now()
    return render(request,'app2/apptwo.html',{'dt':d})

def django(request):
    student ={'name':['raj','divyesh','gyan','rajnish']}
    return render(request,'app2/apptwo.html',student)