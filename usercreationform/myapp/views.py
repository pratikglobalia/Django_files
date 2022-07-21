# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.
# def sign_up(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request,'reg.html',{'form':fm})



from django.shortcuts import render
from .forms import Signupform
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Data save successfully')
            fm.save()
    else:
        fm = Signupform()
    return render(request,'reg.html',{'form':fm})