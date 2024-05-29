from .models import *
from datetime import datetime, timedelta
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
last24H = datetime.now() - timedelta(hours=24)
from django.utils import timezone
from .forms import *
from Visit_Clinic.models import Pateint_Visit_Clinic_Case
from django.contrib.auth.models import User
from Ward.models import Admission_Section
from django.utils import timezone

def get_user_requ(request):
    usr = request.user.id
    usr_id = User.objects.get(id =usr)
    
    
    return usr_id
def Nurse_station_Home(request ):
    Visit_List = Pateint_Visit_Clinic_Case.objects.filter(Visit_id__is_admission = False , is_Close = False)
    sectionlist = Admission_Section.objects.all()
    Nurse_station_Pateiant_count = Pateint_Visit_Clinic_Case.objects.filter(Visit_Date__gte=last24H ).count()
    Vital_Wating = Pateint_Visit_Clinic_Case.objects.filter(Visit_Date__gte=last24H , is_Close = False ).count()
    Vital_Susses = Pateint_Visit_Clinic_Case.objects.filter(Visit_Date__gte=last24H , is_Close = True).count()
    Visit_order = Patiant_Visit_Order.objects.filter(ins_user_date__gte=last24H , ).order_by('-id')
    queryset = Pateint_Visit_Clinic_Case.objects.filter(Visit_id__is_admission = False , is_Close = False)
    Vital_Signs_Form_View = Vital_Signs_Form(request.POST)
    usr = request.user
    print(usr)
    page = request.GET.get('page',1)
    paginator = Paginator(queryset,10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    paginators = Paginator(Visit_order, 10) 
    page_number = request.GET.get('page')
    page_obj = paginators.get_page(page_number)
    context = {
      'Vital_Wating': Vital_Wating ,'Vital_Susses': Vital_Susses ,
      'Nurse_station_Pateiant_count': Nurse_station_Pateiant_count ,
       'Visit_order':Visit_order,
       'page_obj': page_obj , "data": data ,
       'Vital_Signs_Form_View':Vital_Signs_Form_View ,
       'queryset':queryset ,
       'sectionlist':sectionlist

          }
    return context

