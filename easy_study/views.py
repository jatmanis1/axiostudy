import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import logging
from users import models
from users.models import Subject, Unit, Course, Part
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorator import user_verified
from users.models import UserProfile


# from api import active_companies_dict
#from autoslug import AutoSlugField

@user_verified
def index(request):
    return render(request, 'index.html')
def verify(request):
    return render(request, 'verify.html')

def test2(request):
    courses = Course.objects.all()
    units = Unit.objects.all()
    subjects = Subject.objects.all()
    parts = Part.objects.all()
    subject = 1
    data={}
    if subject:
        units = Unit.objects.all()
        for i in units:
            i.course = Course.objects.get(id = i.u_course)
            i.part = Part.objects.get(id = i.u_part)
            i.subject = Subject.objects.get(id = i.u_subject)
        data['units']=units
    data['courses']= courses
    data['parts']= parts
    data['subjects']=subjects
    return render(request, 'test2.html', data)
def test3(request):
    courses = Course.objects.all()
    units = Unit.objects.all()
    subjects = Subject.objects.all()
    parts = Part.objects.all()
    subject = 1
    data={}
    if subject:
        units = Unit.objects.all()
        for i in units:
            i.course = Course.objects.get(id = i.u_course)
            i.part = Part.objects.get(id = i.u_part)
            i.subject = Subject.objects.get(id = i.u_subject)
        data['units']=units
    data['courses']= courses
    data['parts']= parts
    data['subjects']=subjects
    return render(request, 'test3.html', data)
@login_required
def jatmanis1(request):
    user_id = request.user.id 
    user = User.objects.filter(id =  user_id).first()
    print(user.userprofile.is_verified)
    # context['cust']= cust
    # for i in cust:
    #     print(i.name,i.id, i.username, i.password)
    # print(context)
    return render(request, "jatmanis1.html")

@login_required
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
    data['parts']= parts
    data['subjects']=subjects
    return render(request, 'notes.html', data)

@login_required
@user_verified
def reader(request,u_id):
    unit = Unit.objects.filter(id = u_id)
    units = Unit.objects.all()
    data={}
    data['unit']=unit
    data['units']=units
    return render(request, 'reader.html', data)
    



