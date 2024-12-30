import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import logging
from users import models
from users.models import Subject, Unit, Course, Part
from django.urls import reverse
# from api import active_companies_dict
#from autoslug import AutoSlugField
def jatmanis1(request):
    custs = models.Cust.objects.all()
    print(custs)
    user_id = request.user.id 
    user = User.objects.filter(id =  user_id).first()
    cust = models.Cust.objects.filter(username = user.username).first()
    print(user)
    context = {'cust':cust}
    # context['cust']= cust
    # for i in cust:
    #     print(i.name,i.id, i.username, i.password)
    print(context)
    return render(request, "jatmanis1.html",context=context)


def notes(request):
    file_id = '1pTXenILTh_IzlNIWc7qHKF62kk0VsfSc'
    embed_url = f'https://docs.google.com/document/d/{file_id}/preview?usp=embed_google&quality=high'
    return render(request, 'test2.html', {'embed_url': embed_url})


def reader(request,u_id):
    unit = Unit.objects.filter(id = u_id)
    units = Unit.objects.all()
    print(unit)
    for i in units:
        print(i.u_name,i.id)
    data={}
    data['unit']=unit
    data['units']=units
    return render(request, 'reader.html', data)
    



