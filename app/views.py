from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registration(request):
    EUFO=Userform()
    EPFO=Profileform()
    d={'EUFO':EUFO,'EPFO':EPFO}
    
    return render(request,'registration.html',d)