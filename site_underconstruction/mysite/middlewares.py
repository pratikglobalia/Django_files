from django.http import HttpResponse


class UnderConstruction:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        return HttpResponse('Site is under constuction')
        response = self.get_response(request)
        return response