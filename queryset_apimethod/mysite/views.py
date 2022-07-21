from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # students = Student.objects.all()
    
    # students = Student.objects.filter(marks=80)
    
    # students = Student.objects.exclude(marks=80)
    
    # students = Student.objects.order_by('city')
    # students = Student.objects.order_by('-city')
    # students = Student.objects.order_by('?')

    # students = Student.objects.order_by('id').reverse()[:3]
    
    # students = Student.objects.values()
    # students = Student.objects.values('name', 'city')
    
    # students = Student.objects.values_list()
    # students = Student.objects.values_list('id','name',named=True)
    
    # students = Student.objects.dates('pass_date','month')
   
#######################   second table  ########################
    
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # students = qs2.union(qs1)
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # students = qs2.union(qs1, all=True)
    
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # students = qs2.intersection(qs1)
    
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # students = qs1.difference(qs2)
    
#######################   AND  OR  Operater   ########################     

    # students = Student.objects.filter(id=3) & Student.objects.filter(roll=103)
    # students = Student.objects.filter(id=3, roll=103)
    # students = Student.objects.filter(Q(id=3) & Q(roll=103))
    
    # students = Student.objects.filter(id=3) | Student.objects.filter(roll=10)
    students = Student.objects.filter(Q(id=3) | Q(roll=101))
    
    print('Return :', students)
    print()
    print('SqlQuery :',students.query)
    return render(request, 'home.html', {'students':students})