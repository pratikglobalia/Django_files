from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Matchpass

# Create your views here.
def thankyou(request):
    return render(request,'thanks.html')

def passmatch(request):
    if request.method == 'POST':
        fm = Matchpass(request.POST)
        if fm.is_valid():
            return HttpResponseRedirect('/thn/')
        
    else:
        fm = Matchpass()
    
    return render(request,'home.html',{'form':fm})