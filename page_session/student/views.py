from django.shortcuts import render, HttpResponse

# Create your views here.
def set_session(request):
    request.session['name'] = 'pratik'
    return render(request,'setsession.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session['name']
        cage = request.session.get_session_cookie_age()
        age = request.session.get_expiry_age()
        date = request.session.get_expiry_date()
        browse = request.session.get_expire_at_browser_close()
        request.session.modified = True
        return render(request,'getsession.html', {'nm':name, 'cage':cage, 'age':age, 'date':date, 'browse':browse})
    else:
        return HttpResponse('session has expired')

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'delsession.html')