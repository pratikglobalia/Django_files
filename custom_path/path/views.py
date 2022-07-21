from django.shortcuts import render

# Create your views here.
def show_detail(request,year):
    return render(request,'show.html', {'yr':year})
