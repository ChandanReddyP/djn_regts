from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registration(request):
    EUFO=Userform()
    EPFO=Profileform()
    d={'EUFO':EUFO,'EPFO':EPFO}
    
    if request.method=='POST' and request.FILES:
        NMUFDO=Userform(request.POST)
        NMPFDO=Profileform(request.POST,request.FILES)
        
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MFUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MFUFDO.setpassword(pw)
            MFUFDO.save()

            MFPFDO=NMPFDO.save(commit=False)
            MFPFDO.Username=NMUFDO
            MFPFDO.save()

            return HttpResponse('data inserted successfully')
        
        else:

            raise HttpResponse('invalid data')
    
    return render(request,'registration.html',d)