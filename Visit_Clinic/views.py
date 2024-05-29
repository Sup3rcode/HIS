from django.shortcuts import render
from Patient_Visit.models import *
from labotory.models import *
from django.shortcuts import render , redirect , get_object_or_404 
from django.template.loader import render_to_string
from django.http import JsonResponse , HttpResponse
from App_Home.models import *
from .models import *
from datetime import datetime, timedelta
from .forms import *
last24H = datetime.now() - timedelta(hours=24)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from django.contrib.auth.decorators import login_required
from Admission.models import *
import pytz
from accounts.decorators import His_decorators





@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def index(request):
    visit_clinic_list = Clinic_List.objects.filter(User_Access = request.user)
    data  = Pateint_Visit_Clinic_Case.objects.filter(Visit_id__is_admission = False ,is_Close = False , Clinic_Name__User_Access = request.user ).order_by('-id')
    return render(request, 'Clinic_Visit/home.html' , {'visit_clinic_list': visit_clinic_list , 'data':data})


def Get_Visit_By_Clinic_Name(request):
    if request.method == "GET":
        theid = request.GET.get('id_clinic')
        data  = Pateint_Visit_Clinic_Case.objects.filter(Clinic_Name__id__icontains=theid , Visit_id__is_admission = False ,is_Close = False ).order_by('-id')
        #data  = Pateint_Visit_Clinic_Case.objects.filter(Clinic_Name__id__icontains=theid , is_admission = False).order_by('-id')
        data1 = render_to_string('Clinic_Visit/Clinic_List_2.html',{'data': data},request=request)
        return JsonResponse(data1 , safe=False)



def get_visit(request):
    if request.method == "GET":
        visit_id = request.GET.get('visit_id')
        data = get_object_or_404(Pateint_Visit_Clinic_Case, id=visit_id)
        Visit_History_id = Patiant_Visit_History.objects.filter (visit_Case = data)
        Visit_order_list = Patiant_Visit_Order.objects.filter (visit_Case = data)
        admi = Patiant_File_NO.objects.filter(id = data.Patiant_No.id).last()
        Visit_xray = Patiant_Visit_Xray.objects.filter (patiant_no = admi)
        
        Visit_lab_list = Tube_Barcode_Number.objects.filter (Tube_Visit_Number = data)
        
        data = render_to_string('Clinic_Visit/Get_Patient_Visit_History.html',{'Visit_History_id': Visit_History_id , 'Visit_order_list':Visit_order_list ,  'Visit_xray':Visit_xray, 'Visit_lab_list':Visit_lab_list},request=request)
        return JsonResponse(data , safe=False)

@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Visit_Case_View(request, visit_id):
    data = get_object_or_404(Pateint_Visit_Clinic_Case, id=visit_id)
    Transfer_Clinic_list = Clinic_List.objects.all().exclude(id=data.Clinic_Name.id)
    data.Visit_Opened_status = True
    data.Opened_Date = timezone.now()
    data.Open_By_User = request.user
    data.save()
    Vital_Signs_view = Visit_Vital_Signs.objects.filter(visit_Case = data)
    Visit_order = Patiant_Visit_Order.objects.filter (visit_Case = data)
    visit_screan_id = Patiant_Visit_History.objects.filter (visit_Case = data)
    get_visit_list =Pateint_Visit_Clinic_Case.objects.filter(Patiant_No__id=data.Patiant_No.id)
    context = { 'Transfer_Clinic_list':Transfer_Clinic_list ,'vital':Vital_Signs_view  ,'visit_screan_id':visit_screan_id , 'Visit_order':Visit_order ,'data':data}
    return render(request,'Clinic_Visit/Patiant_Visit_Case.html',context)


@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Visit_Case_View2(request, visit_id):
    data = get_object_or_404(Pateint_Visit_Clinic_Case, id=visit_id)
    context = {'data':data}
    return render(request,'Clinic_Visit/all_visit.html',context)

@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Visit_Case_Save(request):
    form = Patiant_Visit_Case_Form(request.POST)
    if request.method == "POST":
        visit_id = request.POST.get('visit_Case_id')
       
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        if form.is_valid():
            Case_Form = form.save(commit=False)
            Case_Form.visit_Case = visit_petiant
            Case_Form.ins_user_code = request.user
            Case_Form.ins_user_date = timezone.now()
            Case_Form.save()
            visit_petiant.Clinic_Visit_status = True
            visit_petiant.save()
            data1 =Patiant_Visit_History.objects.filter(visit_Case = visit_petiant )
            data = render_to_string('Clinic_Visit/list/list_history_id.html',{'visit_screan_id': data1},request=request)
            return JsonResponse(data , safe=False)

@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Visit_Order_Save(request):
    form = Patiant_Visit_Order_Form(request.POST)
    if request.method == "POST":
        visit_id = request.POST.get('visit_Order_id')
      
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        if form.is_valid():
            Order_Form = form.save(commit=False)
            Order_Form.visit_Case = visit_petiant
            Order_Form.ins_user_code = request.user
            Order_Form.ins_user_date = datetime.now()
            Order_Form.save()
            data1 =Patiant_Visit_Order.objects.filter(visit_Case = visit_petiant )
            data = render_to_string('Clinic_Visit/list/list_history_order.html',{'Visit_order': data1},request=request)
            return JsonResponse(data , safe=False)


@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Case_Admission_Save(request):
    form = Patient_Admission_Case_Form(request.POST)
    if request.method == "POST":
        visit_id = request.POST.get('visit_Case_id')
   
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        get_visit = Pateint_Visit.objects.get(id=visit_petiant.Visit_id.id)
       
        patiant_no = Patiant_File_NO.objects.get(id = visit_petiant.Patiant_No.id) 
        get_visit.is_admission = True
        get_visit.admission_from_visit_case_id = visit_petiant.id
        get_visit.save()
        if form.is_valid():
            Patiant_Case_Admission_Form = form.save(commit=False)
            Patiant_Case_Admission_Form.Visit_Case = get_visit
            Patiant_Case_Admission_Form.Visit_Clinic = visit_petiant
            Patiant_Case_Admission_Form.patiant_no = patiant_no
            Patiant_Case_Admission_Form.ins_user_code = request.user
            Patiant_Case_Admission_Form.ins_user_date = timezone.now()
            Patiant_Case_Admission_Form.save()
            return redirect('Visit_Clinic:index')
        else:
            return redirect('Visit_Clinic:index')



################## Xray #############




@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Patiant_Visit_Xray_Save(request):
    form = Patiant_Visit_Xray_Form(request.POST)
    if request.method == "POST":
        visit_id = request.POST.get('visit_xray_id')

        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        
        if form.is_valid():
            xray_Form = form.save(commit=False)
            xray_Form.visit_Case = visit_petiant
            xray_Form.ins_user_code = request.user
            xray_Form.ins_user_date = datetime.now()
            xray_Form.xray_status = 'Waiting Reception'
            xray_Form.save()
            data = Patiant_Visit_Xray.objects.filter(visit_Case = visit_petiant ).values()
            return JsonResponse({'data': list(data)})



@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def xray_visit_list_view(request):
    visit_xray = request.GET.get('visit_xray', None)
    data = Patiant_Visit_Xray.objects.filter(visit_Case = visit_xray )
    data_h = {'is_exists':     Patiant_Visit_History.objects.filter(visit_Case = visit_xray ).exists()}
    if data_h['is_exists'] == False:
        data_h['error_message'] = 'Please Regester Patient Visit Screan'
        return JsonResponse(data_h)
    else :
        return render(request, 'Clinic_Visit/list/xray_case_list.html',{"data": data})



def cheack_visit_sc(request):
    visit_id = request.GET.get('id', None)
    data_h = {'is_exists':     Patiant_Visit_History.objects.filter(visit_Case = visit_id ).exists()}
    if data_h['is_exists'] == False:
        data_h['error_message'] = 'Please  Add Visit Screan'
        return JsonResponse(data_h)
    return JsonResponse(data_h)
   
# Waiting Reception  
@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def xray_order_list_view(request):
    data = Patiant_Visit_Xray.objects.filter(ins_user_date__gte=last24H ).order_by('-id')
    xray24 = Patiant_Visit_Xray.objects.filter(ins_user_date__gte=last24H ).count


    return render(request, 'Radiology/xray_order_list.html',{"data": data , 'xray24':xray24 })
@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def xray_order_list_view2(request):
    data = Patiant_Visit_Xray.objects.all().order_by('-id')
    return render(request, 'Radiology/order_list.html',{"data": data})
@login_required(login_url='login')
@His_decorators( 'Dr_Clinic' )
@login_required(login_url='login')
def xray_report_view(request, visit_id):
    data = get_object_or_404(Patiant_Visit_Xray, id=visit_id)
    Report_Form = Report_Xray_Form(request.POST)
    return render(request,'Radiology/xray_report.html',{'data':data , 'Patiant_order_Xray_Form' : Report_Form})



import json
@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def xray_Reception_Send_To_Report(request):
    visit_xray = request.GET.get('visit_xray', None)
    visit_petiant = Patiant_Visit_Xray.objects.get(id = visit_xray)
    visit_petiant.xray_status = 'Waiting Report'
    visit_petiant.Status_Reception_time = timezone.now()
    visit_petiant.Xray_Order_Status = True

    visit_petiant.save()
    Patiant_Visit_Xray_Report.objects.create(Order_xray=visit_petiant)
    data = {'Saved'}
    return JsonResponse(list(data) , safe=False)
@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Report_Xray_Save(request):
    if request.method == "POST":
        visit_xray = request.POST.get('visit_xray', None)
        
        visit_petiant = Patiant_Visit_Xray.objects.get(id = visit_xray)
        visit_Report = Patiant_Visit_Xray_Report.objects.get(report_order_id = visit_petiant)
        Report_details = request.POST.get('Report_details')
        
        visit_Report.Report_details = Report_details
        visit_Report.Report_time = timezone.now()
        visit_Report.save()
        visit_petiant.Status = 'Finish'
        visit_petiant.save()
        return JsonResponse('ddd' , safe=False)






@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def show_report_xray(request):
    report_id = request.GET.get('report_id', None)
    data =Patiant_Visit_Xray_Report.objects.filter(report_order_id__id = report_id ).last()
    last_pa = data
    Report_details = {'Report_details': data.Report_details , 'Report_time': data.Report_time }
    return JsonResponse(Report_details)



############   Visit Close ################

@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Visit_Close(request):

    if request.method == "POST":
        usr = request.user.id
        usr_id = User.objects.get(id =usr)
        visit_Case_Close = request.POST.get('visit_Case_Close_id')
        Close_Details = request.POST.get('Close_Details')
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_Case_Close)
        visit_petiant.Close_By_User = usr_id
        visit_petiant.Closed_Date = datetime.now()
        visit_petiant.is_Close = True
        visit_petiant.Close_Details = Close_Details
        visit_petiant.save()
        get_visit = Pateint_Visit.objects.get(id = visit_petiant.Visit_id.id)
        get_visit.is_Close = True
        get_visit.Closed_Date = datetime.now()
        get_visit.Close_By_User = usr_id
        get_visit.Close_Details = Close_Details
        get_visit.save()
        return redirect('Visit_Clinic:index')
    else:
            return redirect('Visit_Clinic:index')