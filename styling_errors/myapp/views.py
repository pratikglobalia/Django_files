from django.shortcuts import render
from .forms import Styleerror

# Create your views here.
def error(request):
    if request.method == 'POST':
        fm = Styleerror(request.POST)
        if fm.is_valid():
            print('name :', fm.cleaned_data['name'])
            print('email :', fm.cleaned_data['email'])
            print('password :', fm.cleaned_data['password'])
    else:
        fm = Styleerror()
    
    return render(request,'style.html',{'form':fm})
