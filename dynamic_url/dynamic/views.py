from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

# def unic(request, my_id):
#     return render(request,'show.html',{'id':my_id})

def unic(request, my_id):
    if my_id == 1:
        s = {'id':my_id, 'name':'rohan'}
    if my_id == 2:
        s = {'id':my_id, 'name':'raj'}
    if my_id == 3:
        s = {'id':my_id, 'name':'jeet'}
    return render(request,'show.html', s)

def subunic(request,my_id,my_subid):
    if my_id == 1 and my_subid == 1:
        s = {'id':my_id, 'name':'rohan', 'roll':'101'}
    # if my_id == 2 and my_subid == 2:
    #     s = {'id':my_id, 'name':'raj', 'roll':'102'}
    # if my_id == 3 and my_subid == 3:
    #     s = {'id':my_id, 'name':'jeet', 'roll':'103'}
    return render(request,'show.html', s)