from django.shortcuts import render

# Create your views here.
def hp(request):
    return render(request,'hp.html')
