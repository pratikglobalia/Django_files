from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    template_name = 'mysite/student.html'
    success_url = '/thankyou/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        return form
    
# class StudentCreateView(CreateView):
#     form_class = 'StudentForm
#     template_name = 'mysite/student.html'
#     success_url = '/thankyou/'
    
class ThankYouTemplate(TemplateView):
    template_name = 'mysite/thankyou.html'


class StudentUpdateView(UpdateView):
    model  =Student
    fields = ['name', 'email', 'password']
    template_name = 'mysite/student.html'
    success_url = '/thankyou/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        return form