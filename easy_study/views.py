import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import time
from users import models
# from api import active_companies_dict
#from autoslug import AutoSlugField
def jatmanis1(request):
    custs = models.Cust.objects.all()
    print(custs)
    for i in custs:
        print(i.name, i.username, i.password)
    return render(request, "jatmanis1.html")

def admin(request):
    cust = models.Cust.objects.all()
    data = {}
    data['cust']= cust
    print(data)
    return render(request, 'admin.html', data)