from collections import UserDict
import json
from optparse import Values
from django.shortcuts import render , redirect
from .models import *
from django.http import JsonResponse , HttpResponse
from django.core import serializers
from django.db.models import Q
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
last24H = datetime.now() - timedelta(hours=24)
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import json
# Create your views here.
import barcode
from barcode.writer import ImageWriter
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
def index(request):
    
    return render(request, "index.html")
def index5(request):
    
    return render(request, "login.html")

def index2(request):
    data = Labotory_Test.objects.all()
    return render(request, "lab/lab_list.html",{'data':data})

def Barcode_Search(request):
    if request.method == "GET":
        Barcode_id = request.GET.get('Barcode_id')
        data = Specimens_Arrival_Visit.objects.filter(Barcode_Number__Tube_Number=Barcode_id)
        
        da = Specimens_Arrival_Visit.objects.get(id = data[0].id)
        patiant_name = da.patiant_no.en_patiant_name

        data1 = render_to_string('lab/Barcode_Search.html',{'data': data , 'da':da},request=request)
        return JsonResponse(data1 , safe=False)
     
def Patiant_lab_Tube_List(request):
    if request.method=='GET':
        patiant_no = request.GET.get('patiant_no')
        visit_id = request.GET.get('visit_Case_id')
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        obj = Specimens_Arrival_Visit.objects.filter(Specimens_Visit_Number=visit_petiant )
        for obj in obj :
            data = {'id':obj.id,'Tube_Test_Name':obj.Tube_Test_Name.test_name,'test_tybe':obj.Tube_Test_Name.test_tybe ,}
            ser_instance = json.dumps(data)

            return JsonResponse(ser_instance , safe=False)


def visit_lab_order_list(request):
    if request.method=='POST':
        tybe_id = request.POST.get('tybe_id')
        data = {}
        id_list = request.POST.getlist('id[]')
        patiant_no_lab = request.POST.get('patiant_no_lab')
        visit_id = request.POST.get('visit_Case_id')
        visit_petiant = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        Specimens_Barcode_Number = Tube_Barcode_Number.objects.get(id = tybe_id)
        patiant = Patiant_File_NO.objects.get(id = patiant_no_lab)
        for id in id_list:
            lab_val = Labotory_Test.objects.get(pk=id)
            lab_val2 = Labotory_Test.objects.get(pk=id)
            Specimens_Arrival_Visit.objects.create(Barcode_Number=Specimens_Barcode_Number , Tube_Test_Name = lab_val, Tube_Test_Name2 = lab_val2, Specimens_Visit_Number = visit_petiant  , patiant_no = patiant)
        data = Specimens_Arrival_Visit.objects.filter(Specimens_Visit_Number=visit_petiant , patiant_no = patiant ,)
        data1 = render_to_string('lab/visit_lab_order_list.html',{'data': data},request=request)
        return JsonResponse(data1 , safe=False)

def get_Labotory_Tybe(request):
    if request.method == "GET":
        theid = request.GET.get('term')
        visit_id = request.GET.get('visit_id')

        visit_Tube = Pateint_Visit_Clinic_Case.objects.get(id = visit_id)
        data  = Labotory_Test.objects.filter(Q(test_tybe=theid))
        Labotory_Tube_List.objects.create(Tube_Name = theid , )
        randum_num = number_barcode_function()
        Tube_Barcode_Number.objects.create(Tube_Test_Tybe = theid , Tube_Number = randum_num , Tube_Visit_Number = visit_Tube)
        tybe_id = Tube_Barcode_Number.objects.get(Tube_Number = randum_num).id
        return JsonResponse({'data': list(data.values()) , 'tybe_id': tybe_id})
        #return JsonResponse(list(test_list.values()), safe=False)


def get_Labotory_Tybe_Admission_Case(request):
    if request.method == "GET":
        theid = request.GET.get('term')
        visit_id = request.GET.get('visit_id')
        visit_Tube = Patient_Admission_Case_Visit_Section.objects.get(id = visit_id)
        data  = Labotory_Test.objects.filter(Q(test_tybe=theid))
        Labotory_Tube_List.objects.create(Tube_Name = theid , )
        randum_num = number_barcode_function()
        Tube_Barcode_Number_admission.objects.create(Tube_Test_Tybe = theid , Tube_Number = randum_num , Tube_Visit_Number = visit_Tube)
        tybe_id = Tube_Barcode_Number_admission.objects.get(Tube_Number = randum_num).id
        return JsonResponse({'data': list(data.values()) , 'tybe_id': tybe_id})
        #return JsonResponse(list(test_list.values()), safe=False)

def Specimens_Arrival_View(request):
    lab24 = Specimens_Arrival_Visit.objects.filter(create_time__gte=last24H ).count
    Sampling_status_yes = Specimens_Arrival_Visit.objects.filter(create_time__gte=last24H , is_Done = True ).count
    Sampling_status_no = Specimens_Arrival_Visit.objects.filter(create_time__gte=last24H , is_Done = False ).count
    queryset = Specimens_Arrival_Visit.objects.filter(create_time__gte=last24H ).order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(queryset,10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'lab/Specimens_Arrival_list.html',{"data": data , 'lab24':lab24 , 'Sampling_status_yes':Sampling_status_yes , 'Sampling_status_no':Sampling_status_no })


def Specimens_Reception_Send_To_lab(request):
    visit_lab = request.GET.get('visit_lab', None)
    visit_lab_order = Specimens_Arrival_Visit.objects.get(id = visit_lab)
    visit_lab_order.is_Done = True
    visit_lab_order.save()
    return redirect('labotory:Specimens_Arrival_View')















def Admission_Send_Order_to_lab(request):
    if request.method=='POST':
        tybe_id = request.POST.get('tybe_id')
        data = {}
        id_list = request.POST.getlist('id[]')
        patiant_no_lab = request.POST.get('patiant_no_lab')
        visit_id = request.POST.get('visit_Case_id')
        visit_petiant = Patient_Admission_Case_Visit_Section.objects.get(id = visit_id)
        Specimens_Barcode_Number = Tube_Barcode_Number_admission.objects.get(id = tybe_id)
        patiant = Patiant_File_NO.objects.get(id = patiant_no_lab)
        for id in id_list:
            lab_val = Labotory_Test.objects.get(pk=id)
            lab_val2 = Labotory_Test.objects.get(pk=id)
            Specimens_Arrival_admission.objects.create(Barcode_Number=Specimens_Barcode_Number , Tube_Test_Name = lab_val, Tube_Test_Name2 = lab_val2, Admission_Visit_id = visit_petiant  , patiant_no = patiant)
        data = Specimens_Arrival_Visit.objects.filter(Specimens_Visit_Number=visit_petiant , patiant_no = patiant ,)
        data1 = render_to_string('lab/visit_lab_order_list.html',{'data': data},request=request)
        return JsonResponse(data1 , safe=False)
    
