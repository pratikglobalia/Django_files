from audioop import avg
from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.
def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='rahul')
    # student_data = Student.objects.filter(name__iexact='pratik')
    # student_data = Student.objects.filter(name__contains='P')
    # student_data = Student.objects.filter(name__icontains='P')
    # student_data = Student.objects.filter(id__in=[1,3,4])
    # student_data = Student.objects.filter(marks__in=[88,81,55])
    # student_data = Student.objects.filter(marks__gt=55)
    # student_data = Student.objects.filter(marks__gte=55)
    # student_data = Student.objects.filter(marks__lt=80)
    # student_data = Student.objects.filter(marks__lte=80)
    # student_data = Student.objects.filter(name__startswith='P')
    # student_data = Student.objects.filter(name__istartswith='P')
    # student_data = Student.objects.filter(name__endswith='n')
    # student_data = Student.objects.filter(name__iendswith='n')
    # student_data = Student.objects.filter(passdate__range=('2022-06-01','2022-07-10'))
    # student_data = Student.objects.filter(passdate__year=2022)
    # student_data = Student.objects.filter(passdate__year__gt=2020)
    # student_data = Student.objects.filter(passdate__month=5)
    # student_data = Student.objects.filter(passdate__month__gt=5)
    # student_data = Student.objects.filter(passdate__month__gte=5)
    # student_data = Student.objects.filter(passdate__month__gt=5)
    
#################    aggregate()    ###################
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    min_value = student_data.aggregate(Min('marks'))
    max_value = student_data.aggregate(Max('marks'))
    totalcount = student_data.aggregate(Count('marks'))
    
    context = {'students':student_data,'average':average,'total':total,'minimum':min_value,'maximum':max_value,'totalcount':totalcount}
    print('Return :',student_data)
    return render(request,'home.html', context)