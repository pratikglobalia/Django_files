from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registration


# Create your views here.
def thankyou(request):
    return render(request,'succes.html')

def userdata(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            print('Form validate')
            print('Name', fm.cleaned_data['name'])
            print('Name', fm.cleaned_data['email'])
            return HttpResponseRedirect('/reg/succes/')
            
    else:
        fm = Registration()
    
    return render(request,'userhome.html',{'form':fm})