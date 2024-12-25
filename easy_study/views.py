import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

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
