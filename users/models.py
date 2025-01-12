from django.db import models
from django.contrib.auth.hashers import make_password, check_password


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=True)  # Custom field
    mobile_no = models.CharField(max_length=15, default=1234567890)  # Mobile number
    



class Course(models.Model):
    c_name = models.CharField(max_length=255)  
    c_desc = models.CharField(max_length=255, null=True) 
    

class Part(models.Model):
    p_name = models.CharField(max_length=255 )  
    p_desc = models.CharField(max_length=255, null=True) 

class Subject(models.Model):
    s_name = models.CharField(max_length=255)  
    s_desc = models.CharField(max_length=255, null=True) 
    
class Unit(models.Model):
    u_name = models.CharField(max_length=255)  
    u_owner= models.CharField(max_length=255, default='jatmanis1') 
    u_desc = models.CharField(max_length=255, null=True) 
    u_link = models.URLField()
    u_part = models.IntegerField()
    u_course = models.IntegerField()
    u_subject = models.IntegerField()