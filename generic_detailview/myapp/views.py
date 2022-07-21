from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentDetailView(DetailView):
    model = Student
    # template_name = 'myapp/students.html'
    # context_object_name = 'stu'      #replace student to stu
    # pk_url_kwarg = 'id'     #replace pk to id

    
class StudentListView(ListView):
    model = Student