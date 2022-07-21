import imp
from django.shortcuts import render
from .forms import Registration
from django.contrib import messages

# Create your views here.
def create(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid:
            fm.save()
            messages.success(request,'Successfully')
            fm = Registration()
    else:
        fm = Registration()
    return render(request,'msg.html', {'form':fm})