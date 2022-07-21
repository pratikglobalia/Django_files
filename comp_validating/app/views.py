from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import Formvalidation

# Create your views here.
def thankyou(request):
    return render(request,'thank.html')

def uservalidation(request):
    if request.method == 'POST':
        fm = Formvalidation(request.POST)
        if fm.is_valid():
            d= {
                'name': fm.cleaned_data['name'],'email': fm.cleaned_data['email']
                }
            # return HttpResponseRedirect('thank/')
            return render(request,'thank.html',{'form':d})


    else:
        fm = Formvalidation()
    return render(request,'home.html',{'form':fm})
