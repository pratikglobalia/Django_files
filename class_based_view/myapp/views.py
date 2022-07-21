from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ContactForm

# Create your views here.
# class MyView(View):
#     def get(self,request):
#         return HttpResponse('hello class based view')


# class MyView(View):
#     name = 'Pratik'
#     def get(self,request):
#         return HttpResponse(self.name)    
# class MySubView(MyView):
#     def get(self,request):
#         return HttpResponse(self.name)


class HomeClassView(View):
    def get(self,request):
        context = {'msg':'Welcome to my page'}
        # return render(request,'home.html')
        return render(request,'home.html', context)

class ContactClassView(View):
    def get(self,request):
        fm = ContactForm()
        return render(request,'contact.html', {'form':fm})
    
    def post(self,request):
        if request.method == 'POST':
            fm = ContactForm(request.POST)
            if fm.is_valid():
                return HttpResponse('data saved!!!')
            
class NewsClassView(View):
    template_name = ''
    def get(self, request):
        contaxt = {'msg':'Breaking News '}
        return render(request, self.template_name, contaxt)