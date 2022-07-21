from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    resp = render(request,'setcookie.html')
    # resp.set_cookie('name', 'pratik', max_age=60)
    resp.set_signed_cookie('name', 'pratik', salt='nm')
    return resp

def get_cookie(request):
    # nm = request.COOKIES['name']
    # nm = request.COOKIES.get('name')
    # nm = request.COOKIES.get('name','guest')
    nm = request.get_signed_cookie('name', salt='nm')
    return render(request, 'getcookie.html', {'name':nm})


def del_cookie(request):
    resp = render(request,'delcookie.html') 
    resp.delete_cookie('name')
    return resp
