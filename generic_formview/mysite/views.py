from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import ContactForm

# Create your views here.
class ContactFormView(FormView):
    template_name = 'mysite/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name':'exampale'}
    def form_valid(self, form):
        return HttpResponse('msg sent')

class ThankYouView(TemplateView):
     template_name = 'mysite/thankyou.html'