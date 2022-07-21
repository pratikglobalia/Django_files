from django.shortcuts import render

# Create your views here.
def course_info(request):
    return render(request,'course/courseone.html',{'nm':'pratik','cnm':'Django'})