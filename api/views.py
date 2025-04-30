import requests
import time
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.models import Subject, Unit, Course, Part, UserProfile
from easy_study.decorator import user_verified


# Simple Welcome API
@user_verified
def index(request):
    return JsonResponse({'message': 'Welcome to EasyNotes API'})


def verify(request):
    return JsonResponse({'message': 'Please verify your account'})


@login_required
@user_verified
def jatmanis1(request):
    user_id = request.user.id 
    user = User.objects.filter(id=user_id).first()

    if user.is_staff:
        user_verified_status = None
    else:
        user_verified_status = user.userprofile.is_verified

    return JsonResponse({
        'user': user.username,
        'is_staff': user.is_staff,
        'is_verified': user_verified_status,
    })


@login_required
@user_verified
def notes(request):
    # subject_id = request.GET.get('subject')  # optional subject filtering (currently not used)

    courses = list(Course.objects.values())
    subjects = list(Subject.objects.values())
    parts = list(Part.objects.values())
    units = Unit.objects.all()

    unit_data = []
    for i in units:
        unit_data.append({
            'id': i.id,
            'title': i.u_name,
            'course': Course.objects.get(id=i.u_course).c_name,
            'part': Part.objects.get(id=i.u_part).p_name,
            'subject': Subject.objects.get(id=i.u_subject).s_name,
        })

    return JsonResponse({
        'courses': courses,
        'subjects': subjects,
        'parts': parts,
        'units': unit_data
    })


@login_required
@user_verified
def reader(request, u_id):
    unit = get_object_or_404(Unit, id=u_id)

    unit_info = {
        'id': unit.id,
        'title': unit.u_name,
        'link': unit.u_link,

    }
    return JsonResponse({'unit': unit_info})


@user_verified
def test2(request, u_id):
    unit = get_object_or_404(Unit, id=u_id)
    folder_url = unit.u_link

    image = f'{folder_url}/page_1.png'
    images = []
    try:
        response = requests.get(image)

        if response.status_code == 200:
            images = [f"{folder_url}/page_{i:00d}.png" for i in range(1, count1(folder_url) + 1)]
        else:
            folder_url = f"{folder_url}/images"
            images = [f"{folder_url}/page_{i:04d}.png" for i in range(1, count1(folder_url) + 1)]

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({
        'images': images,
        'folder_url': folder_url,
        'total_pages': count1(folder_url),
    })


def count1(folder_url):
    github_api_url = folder_url
    token = 'your_token_here'  # 🔴 Change it later, never hardcode on production
    headers = {"Authorization": f"token {token}"} if token else None

    def fetch_with_rate_limit_handling(url, headers):
        response = requests.get(url, headers=headers)

        if response.status_code == 403:
            reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
            wait_time = reset_time - int(time.time()) + 1
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)
            response = requests.get(url, headers=headers)

        return response

    response = fetch_with_rate_limit_handling(github_api_url, headers)

    try:
        if response.status_code == 200:
            data = response.json()
            return sum(
                1 for item in data
                if item['type'] == 'file' and item['name'].endswith('.png')
            )
        else:
            print(f"Failed to fetch images. Status code: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error processing the response: {e}")
        return 0


from django.http import HttpResponse, Http404
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
import os

def serve_secure_pdf(request, filename):
    # Check if the user is authenticated or has a valid session
    # if not request.user.is_authenticated:
    #     return HttpResponse("Unauthorized", status=401)
    pdf_path = os.path.join('media', filename)
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename={filename}'
            return response
    raise Http404("PDF not found")


from django.http import JsonResponse

def units(request):
    # Mocked unit data (corrected as a list of dicts)
    units = [
        {
            'id': 1,
            'title': 'mlt_w1',
            'course': 'MLT',
            'part': '1',
            'subject': 'MLT',
        },
        {
            'id': 2,
            'title': 'mlt_w2',
            'course': 'jk',
            'part': '1',
            'subject': 'MT',
        },
        {
            'id': 3,
            'title': 'mlt_w3',
            'course': 'jk',
            'part': '1',
            'subject': 'MT',
        },
        {
            'id': 4,
            'title': 'mlt_w4',
            'course': 'jk',
            'part': '1',
            'subject': 'MT',
        },
        {
            'id': 5,
            'title': 'mlt_w5',
            'course': 'MLT',
            'part': '1',
            'subject': 'MLT',
        },
        {
            'id': 6,
            'title': 'mlt_w6',
            'course': 'MT',
            'part': '1',
            'subject': 'MT',
        },
    ]

    return JsonResponse({'units': units})
from django.http import JsonResponse, Http404

import os
from django.http import HttpResponse, Http404

def unit(request, idx):
    units = [
        {'id': 1, 'title': 'mlt_w1', 'course': 'MLT', 'part': '1', 'subject': 'MLT'},
        {'id': 2, 'title': 'mlt_w2', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 3, 'title': 'mlt_w3', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 4, 'title': 'mlt_w4', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 5, 'title': 'mlt_w5', 'course': 'MLT', 'part': '1', 'subject': 'MLT'},
        {'id': 6, 'title': 'mlt_w6', 'course': 'MT',  'part': '1', 'subject': 'MT'},
    ]

    try:
        idx = int(idx) - 1
        unit = units[idx]
    except (IndexError, ValueError):
        raise Http404("Unit not found")

    filename = unit['title'] + '.pdf'
    pdf_path = os.path.join('media', filename)

    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename={filename}'
            return response

    raise Http404("PDF not found")


def unitdata(request, idx):
    units = [
        {'id': 1, 'title': 'mlt_w1', 'course': 'MLT', 'part': '1', 'subject': 'MLT'},
        {'id': 2, 'title': 'mlt_w2', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 3, 'title': 'mlt_w3', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 4, 'title': 'mlt_w4', 'course': 'jk',  'part': '1', 'subject': 'MT'},
        {'id': 5, 'title': 'mlt_w5', 'course': 'MLT', 'part': '1', 'subject': 'MLT'},
        {'id': 6, 'title': 'mlt_w6', 'course': 'MT',  'part': '1', 'subject': 'MT'},
    ]

    try:
        idx = int(idx) - 1
        unit = units[idx]
    except (IndexError, ValueError):
        raise Http404("Unit not found")

    unit = units[idx]
    return JsonResponse({
        'id': unit['id'],
        'title': unit['title'],
        'course': unit['course'],
        'part': unit['part'],
        'subject': unit['subject'],
    })
    # filename = unit['title'] + '.pdf'
    # pdf_path = os.path.join('media', filename)

    # if os.path.exists(pdf_path):
    #     with open(pdf_path, 'rb') as f:
    #         response = HttpResponse(f.read(), content_type='application/pdf')
    #         response['Content-Disposition'] = f'inline; filename={filename}'
    #         return response

    raise Http404("PDF not found")