from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import StudentModel

# Create your views here.
class StudentCreateView(CreateView):
    model = StudentModel
    fields = ['name', 'email', 'password']
    success_url = '/create/'