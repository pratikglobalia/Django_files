from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'Pushpa', 30)
#         mv = cache.get('movie')
#     return render(request,'course.html', {'fm':mv})


# def home(request):
#     mv = cache.get_or_set('fees', 2000, 20)
#     return render(request,'course.html', {'fm':mv})


def home(request):
    print('_______________________________home____________________')
    data = {'name':'pratik', 'roll':1001}
    cache.set_many(data)
    sv = cache.get_many(data)
    return render(request,'course.html', {'fm':sv})