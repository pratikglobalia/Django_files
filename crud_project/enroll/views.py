from django.shortcuts import render,HttpResponseRedirect
from .forms import Registration
from .models import User

# Create your views here.
def add(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid:
            fm.save()
            fm = Registration()
    else:
        fm = Registration()
    dtl = User.objects.all()
    return render(request,'enroll/add.html', {'form':fm,'data':dtl})



def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    
    
def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Registration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = Registration(instance=pi)
    return render(request,'enroll/update.html', {'form':fm})