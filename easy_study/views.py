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

def index(request):
    return render(request, 'index.html')
def test2(request):
    courses = Course.objects.all()
    units = Unit.objects.all()
    return render(request, 'test2.html', {'courses':courses, 'units':units})
def test3(request):
    courses = Course.objects.all()
    
    units = Unit.objects.all()
    return render(request, 'test3.html', {'courses':courses, 'units':units})
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
    subject = request.POST.get('subject')
    data = {}
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    parts = Part.objects.all()
    subject = 1
    if subject:
        units = Unit.objects.all()
        for i in units:
            i.course = Course.objects.get(id = i.u_course)
            i.part = Part.objects.get(id = i.u_part)
            i.subject = Subject.objects.get(id = i.u_subject)
        data['units']=units
    data['courses']= courses
    data['part']= parts
    data['subjects']=subjects
    return render(request, 'notes.html', data)


def reader(request,u_id):
    unit = Unit.objects.filter(id = u_id)
    units = Unit.objects.all()
    data={}
    data['unit']=unit
    data['units']=units
    return render(request, 'reader.html', data)
    



