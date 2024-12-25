from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Cust
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, 'welcome')
        
        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif not mobile_number.isdigit:
            messages.error(request,  'mobile number must be intiger')
        elif len(mobile_number) != 10:
            messages.error(request, 'mobile number must be 10 digit')
        else:
            # Create user if validation passes
            
            user = Cust(
                username=username,
                name=name,
                email=email,
                mobile_no = mobile_number,
                password=make_password(password)  # Hash the password
            )
            user.save()
            user1 = User(
                username=username,
                email=email,
                password=make_password(password)  # Hash the password
            )
            user1.save()
            messages.success(request, "Your account has been created successfully!")
            # return redirect('login')  # Redirect to the login page after successful registration
    return render(request, 'signup.html')

    
    
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        print(user)  # Debugging to check if the user is found
        
        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)  # This is correct
            return redirect(reverse('jatmanis1'))
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')
