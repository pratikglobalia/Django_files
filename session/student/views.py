from email.policy import default
from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name'] = 'pratik'
    request.session['lname'] = 'patel'
    return render(request,'setsession.html')

    
def get_session(request):
    # name = request.session['name']
    # name = request.session.get('name',default='Guest')
    # lname = request.session['lname']
    # keys = request.session.keys()
    # items = request.session.items()
    # age = request.session.setdefault('age','23')
    # return render(request,'getsession.html', {'nm':name, 'ln':lname, 'keys':keys, 'items':items})
    name = request.session['name']
    cage = request.session.get_session_cookie_age()
    age = request.session.get_expiry_age()
    date = request.session.get_expiry_date()
    browse = request.session.get_expire_at_browser_close()
    return render(request,'getsession.html', {'nm':name, 'cage':cage, 'age':age, 'date':date, 'browse':browse})


def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'delsession.html')