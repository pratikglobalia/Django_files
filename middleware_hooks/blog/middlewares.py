from django.http import HttpResponse

class ProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print('process view before ')
        # return HttpResponse('process view')
        return None
    
    
class ExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        msg = exception
        return HttpResponse(msg)
    
      
class TemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response 
    
    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print('This is process template middleware')
        response.context_data['name'] = 'Raj'
        return response
    