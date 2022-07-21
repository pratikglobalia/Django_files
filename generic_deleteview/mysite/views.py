from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from .forms import StudentForm

# Create your views here.

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'mysite/student.html'
    success_url = '/thankyou/'
    
class ThankYouTemplate(TemplateView):
    template_name = 'mysite/thankyou.html'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'mysite/student.html'
    success_url = '/thankyou/'
    
class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/create/'