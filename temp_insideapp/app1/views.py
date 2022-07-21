from django.shortcuts import render

# Create your views here.
def infoapp1(request):
    return render(request,'app1/info.html',{'nm':'django'})