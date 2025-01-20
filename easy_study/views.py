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
import time
from django.core.paginator import Paginator

# from api import active_companies_dict
#from autoslug import AutoSlugField

@user_verified
def index(request):
    return render(request, 'index.html')
def verify(request):
    return render(request, 'verify.html')

# def test2(request):
#     courses = Course.objects.all()
#     units = Unit.objects.all()
#     subjects = Subject.objects.all()
#     parts = Part.objects.all()
#     subject = 1
#     data={}
#     if subject:
#         units = Unit.objects.all()
#         for i in units:
#             i.course = Course.objects.get(id = i.u_course)
#             i.part = Part.objects.get(id = i.u_part)
#             i.subject = Subject.objects.get(id = i.u_subject)
#         data['units']=units
#     data['courses']= courses
#     data['parts']= parts
#     data['subjects']=subjects
#     return render(request, 'test2.html', data)
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
    print(user)
    if not user.is_staff: 
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
    


def test2(request):
    
    # Base URL for your hosted images
    github_url_base = 'https://jatmanis1.github.io/notes/1%20COMPLEX%20NUMBERS/'
    
    #
    # https://github.com/jatmanis1/notes/blob/main/Accelerator%20nuclear%20physics%20notes%20bsc%20and%20bsc%20bed/page_1.png
    folder_url= 'https://api.github.com/repos/jatmanis1/notes/contents/B.Sc.%202%20Inorganic%20Chemistry%20Exam%202023%20UNIT%20WISE%20Question'
    # folder_url= 'https://api.github.com/repos/jatmanis1/notes/contents/1%20COMPLEX%20NUMBERS'
    print(count1(folder_url))
    images = [f"{folder_url}/page_{i:00d}.png" for i in range(1, count1(folder_url)+1)]  # List of image URLs
    image = f"{folder_url}/page_1.png"
    # print(images)
    # for i in images:
    #     print(i)
    # images_with_webp = [{'original': image, 'webp': image.replace('.jpg', '.webp')} for image in images]
    # paginator = Paginator(images, 4)  # Show 4 images per page
    # page_number = request.GET.get('page')  # Get the current page number from the query string
    # page_obj = paginator.get_page(page_number)
    data={'images1':images}
    # data["page_obj"]= page_obj
    data['folder_url']=folder_url
    token = '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'
    return render(request, 'test2.html', data)


def count1(folder_url):
    # GitHub API endpoint for the folder contents
    github_api_url = folder_url
    
    # List of common image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']
    
    # Fetch the GitHub token from environment variables
    token = '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' # Make sure the token is stored in your environment variables
    headers = {"Authorization": f"token {token}"} if token else None

    def fetch_with_rate_limit_handling(url, headers):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 403:  # Rate limit exceeded
            reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))  # Get reset time
            wait_time = reset_time - int(time.time()) + 1  # Time to wait before retry
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)  # Wait until reset time
            response = requests.get(url, headers=headers)  # Retry the request
        
        return response
    
    # Fetch the folder contents using GitHub API
    response = fetch_with_rate_limit_handling(github_api_url, headers)

    # If the request is successful
    try:
        if response.status_code == 200:
            data = response.json()
            
            # Count image files based on file extension
            image_count = 0
            for item in data:
                # Check if the item is a file and if it ends with an image extension
                if item['type'] == 'file' and any(item['name'].endswith(ext) for ext in image_extensions):
                    image_count += 1
                    # print(item['name'])
            
            print(f"Number of image files in the folder: {image_count}")
            return image_count
        
        else:
            print(f"Failed to retrieve the folder contents. Status code: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error processing the response: {e}")
        return 0
