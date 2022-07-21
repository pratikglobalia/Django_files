from django.shortcuts import render

# Create your views here.
def set_testcookie(request):
    request.session.set_test_cookie()
    return render(request,'settestcookie.html')


def check_testcookie(request):
    work = request.session.test_cookie_worked()
    return render(request,'checktestcookie.html', {'work':work})


def del_testcookie(request):
    request.session.delete_test_cookie()
    return render(request,'deltestcookie.html')
