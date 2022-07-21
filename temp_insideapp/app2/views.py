from django.shortcuts import render

# Create your views here.
def infoapp2(request):
    return render(request,'app2/info.html',{'nm':'django details'})
