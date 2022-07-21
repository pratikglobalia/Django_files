from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class RedirectClass(RedirectView):
    url = 'https://www.youtube.com'
    
class RedirectViewClass(RedirectView):
    pattern_name = 'new'