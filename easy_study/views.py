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

def admin_course_edit(request):
    c_id = request.GET.get('c_id')
    print(c_id,'cidwww')
    # course = None
    
    course = get_object_or_404(Course, id=c_id)
    if request.method == "POST" and course:
        print(request.POST.get('name'),'mkkkkkkkkk')
        course.c_name = request.POST.get('name')
        course.c_desc = request.POST.get('desc')
        print(course)
        course.save()
    
    # print(course)
    # print(c_id)
    
    data ={}
    data['course']=course
    print(data)
    return render(request, 'admin_course_edit.html',data)
def admin_course_add(request):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    if name:
        Course.objects.create(c_name=name, c_desc=desc)
    return render(request, 'admin_course_add.html')
def admin_course(request):
    # course = get_object_or_404(Course, id=course_id)  # Fetch the course to edit
    courses = Course.objects.all()  # Fetch all courses for the dropdown
    courses = Course.objects.all()
    if not Course.objects.exists():
        Course.objects.create(c_name="global", c_desc="This is the default course.")
    if request.method == 'GET':
        course_id = request.GET.get('c_id')
        print(course_id,'c_id1')
        if course_id:
            redirect_url = reverse('admin_course_edit') + f'?c_id={course_id}'
            return redirect(redirect_url)
        print('no id', course_id)
    print(courses, 'mj')
    data = {}
    data['courses']= courses
    # print(data)
    return render(request, 'admin_course.html', data)

def admin(request):
    cust = models.Cust.objects.all()
    data = {}
    data['cust']= cust
    print(data)
    return render(request, 'admin.html', data)

def notes(request):
    file_id = '1pTXenILTh_IzlNIWc7qHKF62kk0VsfSc'
    embed_url = f'https://docs.google.com/document/d/{file_id}/preview?usp=embed_google&quality=high'
    return render(request, 'test2.html', {'embed_url': embed_url})


def admin_part_edit(request):
    p_id = request.GET.get('p_id')
    print(p_id,'cidwww')
    # course = None
    
    part = get_object_or_404(Course, id=p_id)
    if request.method == "POST" and part:
        print(request.POST.get('name'),'mkkkkkkkkk')
        part.p_name = request.POST.get('name')
        part.p_desc = request.POST.get('desc')
        # print(course)
        part.save()
    
    # print(course)
    # print(c_id)
    
    data ={}
    data['part']=part
    print(data)
    return render(request, 'admin_part_edit.html',data)
def admin_part_add(request):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    if name:
        Part.objects.create(p_name=name, p_desc=desc)
    return render(request, 'admin_part_add.html')
def admin_part(request):
    # course = get_object_or_404(Course, id=course_id)  # Fetch the course to edit
    parts = Part.objects.all()  # Fetch all courses for the dropdown
    # part = Part.objects.all()
    if not Part.objects.exists():
        Part.objects.create(p_name=1, p_desc="This is the default part.")
    if request.method == 'GET':
        part_id = request.GET.get('p_id')
        print(part_id,'p_id1')
        if part_id:
            redirect_url = reverse('admin_course_edit') + f'?p_id={part_id}'
            return redirect(redirect_url)
        # print('no id', p_id)
    print(parts, 'mj')
    data = {}
    data['parts']= parts
    # print(data)
    return render(request, 'admin_part.html', data)

