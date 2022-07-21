
# def my_middleware(get_response):
#     print('One-time initialization')
#     def my_function(request):
#         print('This is before view')
#         response =get_response(request)
#         print('This is after view')
#         return response
#     return my_function


# class MyMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print('One-time initialization')
    
#     def __call__(self,request):
#         print('Before view')
#         response = self.get_response(request)
#         print('after view')
#         return response



class FirstMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('First one-time initialization')

    def __call__(self,request):
        print('First before view')
        response = self.get_response(request)
        print('First after view')
        return response
    
class SecondMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('Second one-time initialization')

    def __call__(self,request):
        print('Second before view')
        response = self.get_response(request)
        print('Second after view')
        return response
    
class ThirdMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('Third one-time initialization')

    def __call__(self,request):
        print('Third before view')
        response = self.get_response(request)
        print('Third after view')
        return response