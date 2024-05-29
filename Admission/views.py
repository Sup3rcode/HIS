from django.shortcuts import render , redirect , get_object_or_404 
from django.contrib.auth.decorators import login_required
from luhn_validator import validate
from django.http import JsonResponse , HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
import json
from django.template.loader import render_to_string
from Patient_Visit.models import *
from .models import *
from .forms import *
from accounts.decorators import His_decorators


@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Befor_Admission_Nurse_View(request, id):
    data = get_object_or_404(Patient_Admission_Case_Visit_Section, id=id)
    vital_sings = Patient_Admission_Vital_Signs.objects.filter(Admission_visit_Case__id = data.id)
    Admission_Nurse_Note = Patient_Admission_Order_Nurse_Note.objects.filter(Admission_visit_Case__id = data.id)
    Vital_Signs_Form = Patient_Admission_Vital_Signs_Form(request.POST)
    Nurse_Note_Form = Patient_Admission_Nurse_Note_Form(request.POST)
    context = { 'vital_sings':vital_sings , 'Admission_Nurse_Note':Admission_Nurse_Note ,'Admission_Nurse_Note':Admission_Nurse_Note ,'Nurse_Note_Form':Nurse_Note_Form ,'Vital_Signs_Form':Vital_Signs_Form , 'data':data}
    return render(request,'addmission/Nurse/service_Befor_Admission.html',context)


def load_Bed(request):
    room_id = request.GET.get('room_id')

    data = Admission_Room_Bed.objects.filter(Room_Num__Room_Number=room_id)
    data1 = render_to_string('addmission/get_bed.html',{'data': data},request=request)
    return JsonResponse(data1 , safe=False)


@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Nurse_Visit_Section_Admission(request , Section_id):
    data = get_object_or_404(Admission_Section, id = Section_id)
    Patient_Visited_False = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id , Asing_To_Bed_Status = False , Visit_is_Closed = False )
    Patient_Visited_List = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id , Accept_OF_Section_Status = False ,  Visit_is_Closed = False , Visit_Status = True)
    Patient_Visited_True = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id , Asing_To_Bed_Status = True , Visit_is_Closed = False)
    Transfer_Patient = Transfer_Patient_To_ِِanother_Section.objects.filter(Transfer_From_Section = Section_id , Transfer_completed_Status = False )
    Accept_OF_Section_Status_False = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id ,Accept_OF_Section_Status = False)
    Patient_Visited_count = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id).count()
    room_list = Admission_Room.objects.filter(Section_Name__id = Section_id)
    Visit_order = Patient_Admission_Order.objects.filter(Admission_visit_Case__Section = Section_id)
    
    return render(request,'addmission/Home/Nurse/index.html',{  'Transfer_Patient':Transfer_Patient,'Patient_Visited_List':Patient_Visited_List,'Visit_order':Visit_order,'Accept_OF_Section_Status_False':Accept_OF_Section_Status_False,'Patient_Visited_count':Patient_Visited_count  ,'Patient_Visited_False':Patient_Visited_False ,'Patient_Visited_True':Patient_Visited_True ,'data':data ,  'room_list':room_list})

def Nurse_Admission_Order_update(request, id):  #this function is called when update data
    data = Patient_Admission_Order.objects.get(id=id)
    sec_id = request.POST.get('Sec_id')
    get_sec = Admission_Section.objects.get(id=sec_id)
    print(sec_id)
    form = Patiant_Admission_Ruuselt_Order_Form(request.POST,request.FILES,instance = data)
    if form.is_valid():
        
        Order_Form = form.save(commit=False)
        Order_Form.Nurse_Result_Time = timezone.now()
        Order_Form.order_status = True
        form.save()
        return redirect('Admission:Nurse_Visit_Section_Admission' , Section_id = get_sec.id )
    else:
        return redirect('App_Home:index')


@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Doctor_Visit_Section_Admission(request , Section_id):
    data = get_object_or_404(Admission_Section, id = Section_id)
    Patient_Section_List = Patient_Admission_Case_Visit_Section.objects.filter(Section = Section_id , Accept_OF_Section_Status = True , Visit_is_Closed = False  )
    
    return render(request,'addmission/Doctor/Section_Home.html',{'Patient_Section_List':Patient_Section_List , 'data':data })

def Section_list_Visit_View(Sec_id):
    sec_list = []
    Sec_app = Admission_Section.objects.all()
    sec_list.append(Sec_app)
    for i in sec_list:
        if i != Sec_id[0]:
           pass

@login_required(login_url='/usres/accounts/login/')

def get_visit(request):
    if request.method == "GET":
        visit_id = request.GET.get('Sec_id')
        data = get_object_or_404(Patient_Admission_Case_Visit_Section, id=visit_id)
        Visit_History_id = Patient_Admission_Doctor_Examination_History.objects.filter (visit_Case = data)
        Visit_order_list = Patient_Admission_Order.objects.filter (visit_Case = data)
        Visit_xray = Admission_Visit_Xray.objects.filter (visit_Case = data)
        
        data = render_to_string('addmission/Home/Doctor/Patient_Admission_Case/Tab_Service/get_visites.html',{'Visit_History_id': Visit_History_id , 'Visit_order_list':Visit_order_list ,  'Visit_xray':Visit_xray},request=request)
        return JsonResponse(data , safe=False)



@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Doctor_Patient_Admission_Visited_Details_view(request , visit_id):
    data = get_object_or_404(Patient_Admission_Case_Visit_Section, id = visit_id)
    Transfer_section_list = Admission_Section.objects.all().exclude(id=data.Section.id)
    Transfer_Tybe_list = Transfer_Tybe.objects.all()
    vital_sings = Patient_Admission_Vital_Signs.objects.filter(Admission_visit_Case__id = data.id).last()
    Visit_order = Patient_Admission_Order.objects.filter(Admission_visit_Case__id = data.id)
    visit_screan_id = Patient_Admission_Doctor_Examination_History.objects.filter(Admission_visit_Case__id = data.id)
    vital = Patient_Admission_Vital_Signs.objects.filter(Admission_visit_Case__id = data.id)
    Admission_Nurse_Note = Patient_Admission_Order_Nurse_Note.objects.filter(Admission_visit_Case__id = data.id)
    xray_list = Admission_Visit_Xray.objects.filter(Admission_visit_Case = data.id )
    Visit_Case_Form = Patient_Admission_Doctor_Visit_Case_Form(request.POST)
    Visit_Order_Form = Patient_Admission_Doctor_Visit_Order_Form(request.POST)
    Transfer_Form = Patient_Admission_Doctor_Transfer_Form(request.POST)
    Discharge_Form = Patient_Admission_Doctor_Discharge_Form(request.POST)
    context = {'Transfer_Tybe_list':Transfer_Tybe_list,'xray_list':xray_list  ,'Transfer_section_list':Transfer_section_list ,'Discharge_Form':Discharge_Form ,'Transfer_Form':Transfer_Form ,'visit_screan_id':visit_screan_id ,'Visit_order':Visit_order ,'vital':vital , 'vital_sings':vital_sings , 'Admission_Nurse_Note':Admission_Nurse_Note ,'Admission_Nurse_Note':Admission_Nurse_Note ,'Visit_Case_Form':Visit_Case_Form ,'Visit_Order_Form':Visit_Order_Form , 'data':data}
    return render(request,'addmission/Home/Doctor/Patient_Admission_Case/Case_index.html',context)




@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Admission_Visited_Details_view(request , visit_id):
    data = get_object_or_404(Patient_Admission_Case_Visit_Section, id = visit_id)
    Patient_NO_Visit_List = Pateint_Visit_Clinic_Case.objects.filter(patiant_no = data.Patient_No )
    Vital = Patient_Admission_Vital_Signs.objects.filter(visit_Case__id = data.Patient_visited_id.id)
    Visit_History = Pateint_Visit_Clinic_Case.objects.filter(visit_Case__id = data.Patient_visited_id.id)
    Visit_Order = Patiant_Visit_Order.objects.filter(visit_Case__id = data.Patient_visited_id.id)
    Visit_Xray = Pateint_Visit_Clinic_Case.objects.filter(visit_Case__id = data.Patient_visited_id.id)
    context = {'Visit_History':Visit_History ,'Visit_Order':Visit_Order ,'Visit_Xray':Visit_Xray ,'Vital':Vital , 'Patient_NO_Visit_List':Patient_NO_Visit_List , 'data':data }
    return render(request,'addmission/Doctor/Patient_Admission_Case.html',context)




def Assgin_Pateont_To_Bed_view(request):
    id_id = request.GET.get('id')
    room_id = request.GET.get('id_room')
    bed_id = request.GET.get('id_bed')
    room_bed = Admission_Room_Bed.objects.get(id=bed_id)
    ROOM_NO_id = Admission_Room.objects.get(id = room_bed.Room_Num.id )
    Assgin_To_Bed = Patient_Admission_Case_Visit_Section.objects.get(id = id_id  )
    sta = Patient_Admission_Case.objects.get(id = Assgin_To_Bed.Admission_Case_id.id )
    sta.status = True
    sta.save()
    Assgin_To_Bed.BED = room_bed
    Assgin_To_Bed.ROOM_NO = ROOM_NO_id
    Assgin_To_Bed.Assgin_To_Bed_Date = timezone.now()
    Assgin_To_Bed.Asing_To_Bed_Status = True
    Assgin_To_Bed.save()
    room_bed.in_Use = True
    room_bed.save()
    return JsonResponse('done' , safe=False)

@login_required(login_url='login')

def Patient_Accepted_Section_Status_view(request):
    id_id = request.GET.get('id')
    Patient_Accepted = Patient_Admission_Case_Visit_Section.objects.get(id = id_id  )
    Patient_Accepted.Accept_OF_Section_Status = True
    Patient_Accepted.Accept_OF_Section_Date = timezone.now()
    Patient_Accepted.save()
    return JsonResponse('done' , safe=False)


@login_required(login_url='login')

def Patient_Accepted_Transfer(request):
    id_id = request.GET.get('id')
    Transfer_Accepted = Transfer_Patient_To_ِِanother_Section.objects.get(id = id_id  )
    Transfer_From_Section = Patient_Admission_Case_Visit_Section.objects.get(id = Transfer_Accepted.Visit_Section_id.id )
    Visit_id = Patient_Admission_Case.objects.get(id = Transfer_Accepted.Visit_Section_id.Admission_Case_id.id )
    get_Visit = Patient_Admission_Case_Visit_Section.objects.filter(Admission_Case_id = Visit_id , Visit_Status = False).update(Visit_Status = True , Visit_Transfer = True)
    Transfer_From_Section.Reason_for_Visit_closed = 'Transfer '
    Transfer_From_Section.Visit_is_Closed = True
    Transfer_From_Section.save
    Transfer_Accepted.Approve_by_Nurse_id = request.user
    Transfer_Accepted.Approve_by_Nurse_Date = timezone.now()
    Transfer_Accepted.Transfer_completed_Status = True
    Transfer_Accepted.save()
    saa = Transfer_Accepted.Transfer_To_Section
    transfer_To = Admission_Section.objects.get(id=saa.id)

    
    return JsonResponse('done' , safe=False)

@login_required(login_url='login')

def Reject_to_doctor_view(request):
    
    admission_id = request.GET.get('admission_id')
    get_admission_id = Patient_Admission_Case.objects.get(id = admission_id  )
    get_visit_id = Pateint_Visit.objects.get(id = get_admission_id.Visit_Case.id )
    get_visit_clinic = Pateint_Visit_Clinic_Case.objects.get(id=get_visit_id.admission_from_visit_case_id)
    get_visit_id.is_admission = False
    get_visit_id.admission_from_visit_case_id = ''
    get_visit_clinic.is_Close = False
    get_visit_clinic.Closed_Date = None
    get_visit_clinic.Close_By_User = None
    get_visit_clinic.Close_Details = ''
    get_visit_id.save()
    get_visit_clinic.save()
    get_admission_id.delete()
    return JsonResponse('done' , safe=False)


@login_required(login_url='login')
def Reject_to_Section_view(request):
    id_id = request.GET.get('id')
    Reject_Patient = Patient_Admission_Case_Visit_Section.objects.get(id = id_id  )
    Patient_Admission_Case_Visit_Section.objects.filter(id = Reject_Patient.Visit_Transfer_id ).update(Visit_is_Closed = False ,Reason_for_Visit_closed = '' ,is_Transfer = False )
    Reject_Patient.delete()
    return JsonResponse('done' , safe=False)
from pipes import Template



class Header_prim(Template):
    model = User
    template_name = "header.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_Doctor'] = self.request.user.has_perm('users.Doctor')
        context['helo'] = 'helo'
        return context





# حفظ القياسات الحيوية
@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Admission_Vital_Signs_View(request):
    form =Patient_Admission_Vital_Signs_Form(request.POST)
    if request.method == "POST":
        id = request.POST.get('id')
        Admission_visit_Case = Patient_Admission_Case_Visit_Section.objects.get(id = id)
        patiant_no = Patiant_File_NO.objects.get(id = Admission_visit_Case.Patient_No.id)
        pressure1 = request.POST.get('pressure_1')
        pressure2 = request.POST.get('pressure_2')
        Blood_pressure = pressure1 + "/" + pressure2
        if form.is_valid():
            Vital_Signs_form = form.save(commit=False)
            Vital_Signs_form.Admission_visit_Case = Admission_visit_Case
            Vital_Signs_form.ins_user_code = request.user
            Vital_Signs_form.patiant_no = patiant_no
            Vital_Signs_form.Blood_pressure = Blood_pressure
            Vital_Signs_form.status = True
            Vital_Signs_form.save()
        return redirect('Admission:Patient_Befor_Admission_Nurse_View' , id=id) 



@login_required(login_url='login')

def Admission_Nurse_Note_View(request):
    form =Patient_Admission_Nurse_Note_Form(request.POST,request.FILES)
    if request.method == "POST":
        id = request.POST.get('id')
        Admission_visit_Case = Patient_Admission_Case_Visit_Section.objects.get(id = id)
        patiant_no = Patiant_File_NO.objects.get(id = Admission_visit_Case.Patient_No.id)
        if form.is_valid():
            Nurse_Note_Form = form.save(commit=False)
            Nurse_Note_Form.Admission_visit_Case = Admission_visit_Case
            Nurse_Note_Form.ins_user_code = request.user
            Nurse_Note_Form.patiant_no = patiant_no
            Nurse_Note_Form.save()
        return redirect('Admission:Patient_Befor_Admission_Nurse_View' , id=id) 

        
from xhtml2pdf import pisa
from django.template.loader import get_template
@login_required(login_url='users:login')
def Nurse_Note_Pdf(request ,id):
	pdf = Patient_Admission_Order_Nurse_Note.objects.get(id = id)
	template_path = 'scanner/nurse_note_pdf.html'
	context = {'pdf':pdf }
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(html, dest=response)
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response



@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Admission_Doctor_Order_View(request):
    form =Patient_Admission_Doctor_Visit_Order_Form(request.POST,request.FILES)
    if request.method == "POST":
        get_Visit_id = request.POST.get('get_Visit_id')
        Admission_visit_Case = Patient_Admission_Case_Visit_Section.objects.get(id = get_Visit_id)
        patiant_no = Patiant_File_NO.objects.get(id = Admission_visit_Case.Patient_No.id)
        if form.is_valid():
            Nurse_Note_Form = form.save(commit=False)
            Nurse_Note_Form.Admission_visit_Case = Admission_visit_Case
            Nurse_Note_Form.ins_user_code = request.user
            Nurse_Note_Form.patiant_no = patiant_no
            Nurse_Note_Form.save()
        return redirect('Admission:Doctor_Patient_Admission_Visited_Details_view' , visit_id=Admission_visit_Case.id) 


@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Admission_Doctor_Visit_Case_View(request):
    form =Patient_Admission_Doctor_Visit_Case_Form(request.POST,request.FILES)
    if request.method == "POST":
        get_Visit_id = request.POST.get('get_Visit_id')
        Admission_visit_Case = Patient_Admission_Case_Visit_Section.objects.get(id = get_Visit_id)
        patiant_no = Patiant_File_NO.objects.get(id = Admission_visit_Case.Patient_No.id)
        if form.is_valid():
            Nurse_Note_Form = form.save(commit=False)
            Nurse_Note_Form.Admission_visit_Case = Admission_visit_Case
            Nurse_Note_Form.ins_user_code = request.user
            Nurse_Note_Form.patiant_no = patiant_no
            Nurse_Note_Form.save()
        return redirect('Admission:Doctor_Patient_Admission_Visited_Details_view' , visit_id=Admission_visit_Case.id) 


@login_required(login_url='login')
@His_decorators('Nrs_Admission' , 'Dr_Admission')
def Patient_Admission_Transfer_View(request):
    if request.method == "POST":
        id = request.POST.get('Visit_id')
        Transfer_To_Section = request.POST.get('Section_id')
        Section_id = Admission_Section.objects.get(id =Transfer_To_Section )
        Transfer_Tybe_post = request.POST.get('Transfer_Tybe')
        Transfer_Tybe_Get = Transfer_Tybe.objects.get(id = Transfer_Tybe_post)
        Transfer_Description_id = request.POST.get('Transfer_Description')
        Admission_visit_Case = Patient_Admission_Case_Visit_Section.objects.get(id = id)
        Admission_visit_Case.is_Transfer = True
        Admission_visit_Case.save()
        Transfer_Done = Transfer_Patient_To_ِِanother_Section.objects.create(
            Visit_Section_id = Admission_visit_Case ,
            Transfer_Tybe = Transfer_Tybe_Get ,
            Transfer_From_Section = Admission_visit_Case.Section ,
            Transfer_To_Section = Section_id , 
            Transfer_Description = Transfer_Description_id ,
            Transfer_By_Doctor_id = request.user ,
            Transfer_By_Doctor_Date = timezone.now()
        )
        Transfer_Done.save()

        return redirect('Admission:Doctor_Visit_Section_Admission' , Section_id.id)








def Patiant_Visit_Xray_Save(request):
    form = Patiant_admission_Xray_Form(request.POST)
    if request.method == "POST":
        visit_id = request.POST.get('visit_xray_id')
        
        visit_petiant = Patient_Admission_Case_Visit_Section.objects.get(id = visit_id)
        _Patient_No = Patiant_File_NO.objects.get(id=visit_petiant.Patient_No.id)
        visit_screan_id = Patient_Admission_Doctor_Examination_History.objects.filter(Admission_visit_Case__id = visit_petiant.id).last()
        
       # Visit_History = Patient_Admission_Doctor_Examination_History.objects.filter(Admission_visit_Case__id = visit_petiant.Admission_Case_id.id).id
       
        if form.is_valid():
            xray_Form = form.save(commit=False)
            xray_Form.Admission_visit_Case = visit_petiant
            xray_Form.patiant_no = _Patient_No
            xray_Form.Visit_History = visit_screan_id
            xray_Form.ins_user_code = request.user
            xray_Form.ins_user_date = datetime.now()
            xray_Form.save()
            xray_list = Admission_Visit_Xray.objects.filter(Admission_visit_Case = visit_petiant )
            data = render_to_string('addmission/Home/Doctor/Patient_Admission_Case/list/xray_case_list.html',{'xray_list': xray_list},request=request)
            return JsonResponse(data , safe=False)



@login_required(login_url='login')

def Patient_Admission_Doctor_Discharge_View(request):
    
    if request.method == "POST":
        get_Visit_id = request.POST.get('Visit_id')
        Discharge_Description = request.POST.get('Discharge_Description')
        Admission_visit_Section = Patient_Admission_Case_Visit_Section.objects.get(id = get_Visit_id)
        Admission_visit = Patient_Admission_Case.objects.get(id = Admission_visit_Section.Admission_Case_id.id)
        Admission_visit.Discharge_status = True
        Admission_visit.End_Admission_Date = datetime.now()
        Admission_visit.Visit_Case_is_Closed = True
        Admission_visit.save()
        Admission_visit_Section.is_Discharge = True
        Admission_visit_Section.Discharge_OF_Section_Status = True
        Admission_visit_Section.Discharge_OF_Section_Date = datetime.now()
        Admission_visit_Section.Discharge_Description = Discharge_Description
        Admission_visit_Section.Discharge_By_User_Code = request.user
        Admission_visit_Section.Visit_is_Closed = True
        Admission_visit_Section.Reason_for_Visit_closed = 'Discharge_Description'
        Admission_visit_Section.save()
        Pateint_Visit.objects.filter(id=Admission_visit.Visit_Case.id).update(is_Close = True , Closed_Date = datetime.now() , Close_By_User = request.user , Close_Details = Discharge_Description )
        Pateint_Visit_Clinic_Case.objects.filter(id = Admission_visit.Visit_Clinic.id ).update(is_Close = True , Closed_Date = datetime.now() , Close_By_User = request.user , Close_Details = Discharge_Description)

        return redirect('Admission:Doctor_Visit_Section_Admission' , Section_id=Admission_visit_Section.Section.id) 

