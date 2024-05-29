from urllib import request
from django.shortcuts import render , redirect
from Patient_Files.models import Patiant_File_NO , Nationality
# Create your views here.

from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from accounts.decorators import His_decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

  
@login_required
@His_decorators('doc' )
def my_view(request):
    #sert = user_is_Doc(user = request.user , Role_Name = 'Doctor' )
    #print(sert)
    return render(request, 'care/index.html')

def index(request):

    return render(request, 'care/index.html')

# جلب بيانات المريض في الإستقبال

def error_404(request, exception):
    data = {"name": "somthing error"}
    return render(request,'404.html', data)