from accounts.models import Role_list
from django.shortcuts import render

from .models import Role_list
from functools import wraps
def His_decorators(*groups):
    def inner(view_func):
        @wraps(view_func)
        
        def wrapper_func(request, *args, **kwargs):
            print(groups)
            for i in groups :
                print(i)
            
                if Role_list.objects.filter(Role_Name__in = groups, user = request.user ).exists():
                    return view_func(request, *args, **kwargs)
                else:
                    return render(request, '503.html')
        return wrapper_func
    return inner