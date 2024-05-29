from accounts.models import Role_list
from django.shortcuts import render


__author__ = "Hossain Chisty"

def _currentUser(Role_Name):
    '''
    This decorator for authenticated users only, and filtering by the logged in user from the request, another user, even if logged in, can't access another user's data.
    '''
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            models = Role_list
            selected_user = models.objects.filter(user=request.user ,Role_Name = Role_Name).exists()
            if selected_user:
                return func(request, *args, **kwargs)
            else:
                return render(request, 'core/error/403.html')

        return wrapper
    return decorator