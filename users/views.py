from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import  UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from .models import UserProfile



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif not mobile_number.isdigit():
            messages.error(request, 'Mobile number must be a number.')
        elif len(mobile_number) != 10:
            messages.error(request, 'Mobile number must be 10 digits.')
        else:
            # Create the user if validation passes
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.first_name = name  # Set first name
            user.save()

            # Create user profile linked to the user
            profile = UserProfile.objects.create(user=user, is_verified=False)

            # Log the user in after successful registration
            login(request, user)

            messages.success(request, "Your account has been created successfully!")
            return redirect('login1')  # Redirect to the login page

    return render(request, 'signup.html')

    
    
def login1(request):
    next_url = request.GET.get('next', None)  # Get the 'next' parameter or use '/' as default
    # print(next_url)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(request.GET.get('next'))
        # next_url = request.GET.get('next', '/')  # Get the 'next' parameter or use '/' as default
        # print(next_url)
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        print(user)  # Debugging to check if the user is found
        
        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)  # This is correct
            print(request.GET.get('next'))
            messages.success(request, 'Login Sucess')
            if not next_url:
                return redirect(reverse('jatmanis1'))
            else:
                return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')
