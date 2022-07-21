from django.shortcuts import render

# Create your views her.
def home(request):
    return render(request,'course.html')
