from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studetail(request):
    stud = Student.objects.all()
    return render(request,'stuinfo.html',{'stu':stud})