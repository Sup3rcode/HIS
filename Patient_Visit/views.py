from django.shortcuts import render , redirect
from .models import *
from django.utils import timezone
import datetime
from django.http import JsonResponse , HttpResponse
from Patient_Files.forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
last24H = datetime.now() - timedelta(hours=24)
from Visit_Clinic.models import Pateint_Visit_Clinic_Case
from accounts.decorators import His_decorators

def pa_range():
    ran = Patiant_File_NO.objects.filter(id__range=(19360 , 19460) , gender = '2')
    for i in ran :
        male = Patiant_File_NO.objects.get(id = i.id)

        Patiant_Mode_i = '4'
        Clinic_Name = '2'
        
        Patiant_Mode_id = Patiant_Mode.objects.get(id=Patiant_Mode_i)
        Clinic_Name_id = Clinic_List.objects.get(id=Clinic_Name)
        user_id= User.objects.get(id='1')
        Pateint_Visit.objects.create(Patiant_No=male,Patiant_Mode=Patiant_Mode_id,Clinic_Name=Clinic_Name_id,ins_user_code=user_id )

@login_required(login_url='login')
@His_decorators('Reception' , '')
def Patient_Visit_Home(request):
    
    return render(request, "Patient_Visit/home.html")


def Last_Patiant_24H(request):
    data = Pateint_Visit_Clinic_Case.objects.filter(Visit_id__is_admission = False ).order_by('-id')

    return render(request, 'Patient_Visit/last-24h.html',{"data": data})

    



def validate_Visit(request):
    Visit_id = request.GET.get('P_id')

    data = {'is_exists':     Pateint_Visit.objects.filter(Patiant_No__id = Visit_id , is_Close = False).exists()}
    if data['is_exists'] == True:
        data['error_message'] = 'يوجد للمريض زيارة سابقة الرجاء إغلاقها '
    return JsonResponse(data)



@login_required(login_url='login')
@His_decorators('Reception' , 'Patient_Files' )
def Send_Pateiant_To_Clinic(request):
    data = dict()
    if request.method == 'POST':
        PaTient_id = request.POST.get('File_id')
        Patiant_Mode_i = request.POST.get('Patiant_Mode')
        Clinic_Name = request.POST.get('Clinic_Name')
        PaTient_file = Patiant_File_NO.objects.get(id=PaTient_id)
        Patiant_Mode_id = Patiant_Mode.objects.get(id=Patiant_Mode_i)
        Clinic_Name_id = Clinic_List.objects.get(id=Clinic_Name)
        user_id= User.objects.get(id=request.user.id)
        Pateint_Visit.objects.create(Patiant_No=PaTient_file,Patiant_Mode=Patiant_Mode_id,Clinic_Name=Clinic_Name_id,ins_user_code=request.user , )
        data= Pateint_Visit.objects.filter(Visit_Date__gte=last24H).order_by('-id').values()
                #data = Clinic_Reception.objects.filter(Login_Date__gte=last24H).order_by('-id')
        return JsonResponse(list(data) , safe=False)



@login_required(login_url='login')
@His_decorators('Reception' , 'Patient_Files' , 'Dr_Clinic' )
def Transfer_Pateiant_To_Clinic(request):
    if request.method == 'POST':
        PaTient_id = request.POST.get('File_id')
        Transfer_Visit_id = request.POST.get('Transfer_Visit_id')
        Clinic_Name = request.POST.get('Transfer_id_clinic')
        Clinic_Name_id = Clinic_List.objects.get(id=Clinic_Name)
        Transfer_Details = request.POST.get('Transfer_Details')
        user_id= User.objects.get(id=request.user.id)
        get_visit = Pateint_Visit_Clinic_Case.objects.get(id=Transfer_Visit_id)
        Close_Details_TR = "Transfer To Clinic " + Clinic_Name_id.Clinic_Name
        Details_TR = "Transfer From Clinic " + get_visit.Clinic_Name.Clinic_Name
        get_visit.is_Transfer = True
        get_visit.Transfer_Date = datetime.now()
        get_visit.Transfer_By_User  = user_id
        get_visit.Transfer_Details = Transfer_Details
        get_visit.is_Close = True
        get_visit.Closed_Date = datetime.now()
        get_visit.Close_By_User = user_id
        get_visit.Close_Details = Close_Details_TR
        get_visit.save()
        id_case = Pateint_Visit.objects.get(id=get_visit.Visit_id.id)
        _Clinic = Clinic_List.objects.get(id=Clinic_Name)
        _Patient_No = Patiant_File_NO.objects.get(id=get_visit.Patiant_No.id)
        Pateint_Visit_Clinic_Case.objects.create(Visit_id=id_case , Visit_Type = Details_TR , is_Transfer = True ,Patiant_No = _Patient_No , Clinic_Name = _Clinic)
        return redirect('Visit_Clinic:index')
    else:
        return redirect('Visit_Clinic:index')
       