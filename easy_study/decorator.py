# from django.http import HttpResponseForbidden
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from users.models import UserProfile


from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden



def user_verified(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                # Retrieve the related customer instance
                user = request.user
                if user.is_staff:
                    return view_func(request, *args, **kwargs)
                elif user.userprofile.is_verified:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('verify')  # Redirect to a "not verified" page
            except user.DoesNotExist:
                return HttpResponseForbidden("User does not have a valid customer profile. 1")
        else:
            return redirect('login')  # Redirect to login page if user is not authenticated
    return _wrapped_view
