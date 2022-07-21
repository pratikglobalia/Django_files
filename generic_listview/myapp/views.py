from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    
    # template_name_suffix = '_get'                   #custom template name
    # ordering = ['roll']                             #order fields
    template_name = 'myapp/student.html'            #custom template 
    # context_object_name = 'students'                #custom object_name

    def get_queryset(self):
        return Student.objects.filter(course='django')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fresher']=Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user'] == 'pratik':
            template_name = 'myapp/pratik.html'
        else:
            template_name = self.template_name
        return [template_name]