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

def admin(request):
    cust = models.Cust.objects.all()
    data = {}
    data['cust']= cust
    print(data)
    return render(request, 'admin.html', data)



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
            redirect_url = reverse('admin_course_edit') + f'/{course_id}'
            return redirect(redirect_url)
        print('no id', course_id)
    print(courses, 'mj')
    data = {}
    data['courses']= courses
    # print(data)
    return render(request, 'admin_course.html', data)


# Part
def admin_part_edit(request,p_id):
    p_id = p_id
    # print(p_id,'cidwww')
    # course = None
    flag = False
    part = Part.objects.filter(id = p_id)[0]
    if request.method == "POST" and part:
        print(request.POST.get('name'),'mkkkkkkkkk')
        part.p_name = request.POST.get('name')
        part.p_desc = request.POST.get('desc')
        # print(course)
        part.save()
    if not part:
        flag = True
        
    # print(course)
    # print(c_id)
    
    data ={}
    data['part']=part
    data['flag']=flag
    # print(data)
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
            redirect_url = reverse('admin_course_edit') + f'/{part_id}'
            return redirect(redirect_url)
        # print('no id', p_id)
    print(parts, 'mj')
    data = {}
    data['parts']= parts
    # print(data)
    return render(request, 'admin_part.html', data)


# Subject

def admin_subject_edit(request,s_id):
    s_id = s_id
    print(s_id,'cidwww')
    # course = None
    flag = False
    
    subject = Subject.objects.filter(id=s_id)[0]
    if request.method == "POST" and subject:
        print(request.POST.get('name'),'mkkkkkkkkk')
        subject.s_name = request.POST.get('name')
        subject.s_desc = request.POST.get('desc')
        # print(course)
        subject.save()
    elif not subject:
        flag = True
    
    # print(course)
    # print(c_id)
    print(subject)
    data ={}
    data['subject']=subject
    data['flag']=flag
    
    print(data)
    return render(request, 'admin_subject_edit.html',data)
def admin_subject_add(request):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    if name:
        Subject.objects.create(s_name=name, s_desc=desc)
    return render(request, 'admin_subject_add.html')
def admin_subject(request):
    
    # course = get_object_or_404(Course, id=course_id)  # Fetch the course to edit
    subjects = Subject.objects.all()  # Fetch all courses for the dropdown
    # part = Part.objects.all()
    if not Subject.objects.exists():
        Subject.objects.create(s_name=1, s_desc="This is the default part.")
    if request.method == 'GET':
        subject_id = request.GET.get('s_id')
        print(subject_id,'p_id1')
        if subject_id:
            redirect_url = reverse('admin_subject_edit', args=[subject_id])
            return redirect(redirect_url)
        # print('no id', p_id)
    print(subjects, 'mj')
    data = {}
    data['subjects']= subjects
    # print(data)
    return render(request, 'admin_subject.html', data)




# Unit
def admin_unit_edit(request,u_id):
    i_id = u_id
    print(u_id,'cidwww')
    # course = None
    flag = False
    
    unit = Unit.objects.filter(id=u_id)[0]
    if request.method == "POST" and unit:
        print(request.POST.get('name'),'mkkkkkkkkk')
        unit.u_name = request.POST.get('name')
        unit.u_desc = request.POST.get('desc')
        unit.u_subject = request.POST.get('u_subject')
        unit.u_course = request.POST.get('u_course')
        unit.u_part = request.POST.get('u_part')
        unit.u_link = request.POST.get('u_link')
        unit.u_owner = request.POST.get('owner')
        # print(course)
        unit.save()
    elif not unit:
        flag = True
    
    # print(course)
    # print(c_id)
    print(unit)
    data ={}
    data['unit']=unit
    data['flag']=flag
    subjects = Subject.objects.all()
    parts = Part.objects.all()
    courses = Course.objects.all()
    data['subjects']= subjects
    data['parts']= parts
    data['courses']= courses
    print(data)
    return render(request, 'admin_unit_edit.html',data)
def admin_unit_add(request):
    u_name = request.POST.get('name')
    u_desc = request.POST.get('desc')
    u_subject = request.POST.get('u_subject')
    u_course = request.POST.get('u_course')
    u_part = request.POST.get('u_part')
    u_link = request.POST.get('u_link')
    owner = request.POST.get('owner')
    subjects = Subject.objects.all()
    parts = Part.objects.all()
    courses = Course.objects.all()
    if u_name:
        Unit.objects.create(u_name=u_name, u_desc=u_desc, u_course=u_course, u_link=u_link,u_part=u_part,u_subject=u_subject,u_owner=owner)
    data={}
    data['subjects']= subjects
    data['parts']= parts
    data['courses']= courses
    
    return render(request, 'admin_unit_add.html',data)
def admin_unit(request):
    
    # course = get_object_or_404(Course, id=course_id)  # Fetch the course to edit
    units = Unit.objects.all()  # Fetch all courses for the dropdown
    # part = Part.objects.all()
    # if not units.objects.exists():
    #     Unit.objects.create(u_name=1, u_desc="This is the default unit.")
    if request.method == 'GET':
        unit_id = request.GET.get('u_id')
        print(unit_id,'u_id1')
        if unit_id:
            redirect_url = reverse('admin_unit_edit', args=[unit_id])
            return redirect(redirect_url)
        # print('no id', p_id)
    print(units[0].u_name, 'mj')
    data = {}
    data['units']= units
    
    # print(data)
    return render(request, 'admin_unit.html', data)

