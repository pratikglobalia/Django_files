from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request,'app/home.html',{'data':'Data of app'})
