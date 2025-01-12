from django.db import models
from django.contrib.auth.hashers import make_password, check_password


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=True)  # Custom field
    mobile_no = models.CharField(max_length=15, default=1234567890)  # Mobile number
    


# class Cust(models.Model):
#     username = models.CharField(max_length=150, unique=True)  # Unique username
#     name = models.CharField(max_length=255)  # Full name
#     # is_verified = models.BooleanField(default=False) 
#     is_verified = models.BooleanField(default=False)

#     mobile_no = models.CharField(max_length=15, unique=True)  # Mobile number
#     email = models.EmailField(unique=True)  # Email address
#     password = models.CharField(max_length=128, default='12345678')  # Password field
#     # verify = models.BooleanField(default=False)
#     def save(self, *args, **kwargs):
#         # Hash the password before saving
#         if not self.password.startswith('pbkdf2_sha256$'):  # Prevent re-hashing already hashed passwords
#             self.password = make_password(self.password)
#         super(Cust, self).save(*args, **kwargs)

#     def checkpw(self, raw_password):
#         """
#         Verifies if the given raw_password matches the stored hashed password.
#         """
#         return check_password(raw_password, self.password)

#     # def __str__(self):
#     #     return self.username

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