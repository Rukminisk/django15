
from django.shortcuts import render

#   Function based view

def Test(request):
    return render(request,'login.html')



