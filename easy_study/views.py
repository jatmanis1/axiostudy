import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import logging
from users import models
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

import requests
from django.http import HttpResponse

def proxy_pdf(request):
    # pdf_url = 'https://p-def6.pcloud.com/DLZfQM0KGZWajDmS7ZlduM7ZZc8whXkZ1ZZcu8ZZsjEJZI4ZjYZqpZJPf0Lt7KNdBcBFHjcbniXprzgsgy/Week_1.pdf'
    # response = requests.get(pdf_url, stream=True)
    # if response.status_code == 200:
    #     return HttpResponse(response.content, content_type='application/pdf')
    # else:
    #     return HttpResponse('Failed to fetch PDF', status=response.status_code)
    return render(request, 'test3.html')

# def stream_gdrive_document(request, file_id):
#     # Google Drive direct download URL
#     gdrive_url = f"https://docs.google.com/document/d/1whr3L1Y8pcNbpJhbtrptlH0hmpo3IG3QyAVhp4Rfroo/preview"
#     # https://docs.google.com/document/d/1whr3L1Y8pcNbpJhbtrptlH0hmpo3IG3QyAVhp4Rfroo/edit?usp=sharing
#     print(gdrive_url)
    
#     # Fetch the file from Google Drive
#     response = requests.get(gdrive_url, stream=True)
#     print(response)
#     # Check if the file exists
#     if response.status_code == 200:
#         # Stream the content to the user
#         content_type = response.headers.get('Content-Type', 'application/pdf')  # Adjust if needed
#         return HttpResponse(response.content, content_type=content_type)
    
#     # Return an error if the file is not found
#     return HttpResponse("File not found", status=404)


