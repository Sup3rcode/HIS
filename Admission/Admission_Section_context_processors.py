from .models import *

from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import *
from django.db import connection
from Admission.forms import *
from Ward.models import *
def my_custom_sql(user , request):
        cursor = connection.cursor()
        cursor.execute("select id,user,host,db,command,time,state,info from information_schema.processlist")
        row = cursor.fetchall()
        print(row)
        return row

def is_member(user, *group_names):
    if user.is_authenticated:
        if bool(user.groups.filter(name__in=group_names)):
            return True
    return False
from django.contrib.auth import login, authenticate, update_session_auth_hash



def get_section_list(request):
    
    if request.user.is_authenticated:
        section_list = Admission_Section.objects.filter(User_Access = request.user )
        return {'section_list':section_list}
    else : 
        section_list = Admission_Section.objects.none()
        return {'section_list':section_list}




def get_section_list2(request):
    Patiant_Count = Patiant_File_NO.objects.all().count()
    Bed_Count = Patient_Admission_Case_Visit_Section.objects.all().count()
    Room_Count = Admission_Room.objects.all().count()
    Reception_Count = Pateint_Visit_Clinic_Case.objects.all().count()
    User_Count = User.objects.all().count()
    return {'User_Count':User_Count ,'Patiant_Count':Patiant_Count , 'Bed_Count':Bed_Count , 'Room_Count':Room_Count , 'Reception_Count':Reception_Count }


def user_permissions(request):
   
    context = {'is_supports':request.user.has_perm('users.support') ,
        'Radiolog':request.user.has_perm('users.Radiology') , 
        'labotory':request.user.has_perm('users.labotory') ,
        'Nurse':request.user.has_perm('users.Nurse') , 
        'is_clients':request.user.has_perm('users.clients') , 
        'New_User':request.user.has_perm('users.New_User') ,
        'is_Receptio':request.user.has_perm('users.Reception') , }
    return context

def Admission_forms(request):
   
    context = {
        'Transfer_Forms':Patient_Admission_Doctor_Transfer_Form ,
        'Discharge_Form':Patient_Admission_Doctor_Discharge_Form , 
          }
    return context