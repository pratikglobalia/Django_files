from django.shortcuts import render

# Create your views here.
def fees_info(request):
    return render(request,'fees/feesone.html',{'fee':'45000'})
