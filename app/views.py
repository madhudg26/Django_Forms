from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def django_forms(request):
    formobject=Student_Details()
    d={'form':formobject}
    if request.method=="POST":
        FD=Student_Details(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            u=FD.cleaned_data['url']
            e=FD.cleaned_data['email']
            t=FD.cleaned_data['time']
            d=FD.cleaned_data['date']
            dt=FD.cleaned_data['datetime']
            pw=FD.cleaned_data['password']
            ad=FD.cleaned_data['address']
            #gen=FD.changed_data['gender']
            d1={'n':n,'a':a,'u':u,'e':e,'t':t,'d':d,'dt':dt,'pw':pw,'ad':ad}
            return render(request,'form_data.html',d1)


    return render(request,'django_forms.html',d)