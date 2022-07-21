from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    stu_data = Student.students.all()
    return render(request,'home.html', {'students':stu_data})