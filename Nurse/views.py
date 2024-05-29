from django.shortcuts import render
from Visit_Clinic.models import Pateint_Visit_Clinic_Case
from django.shortcuts import render , redirect , get_object_or_404
from .forms import *
from Admission.models import *
from django.utils import timezone
from django.http import JsonResponse , HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import His_decorators




@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Home(request):
    Patient_Visited_List = Patient_Admission_Case_Visit_Section.objects.filter(Accept_OF_Section_Status = False ,  Visit_is_Closed = False , Visit_Status = True)
    return render(request, "Visit_Nurse_Service/home.html" , {'Patient_Visited_List':Patient_Visited_List})




@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Nurse_station_Patiant_Visit(request, visit_id):
    data = get_object_or_404(Pateint_Visit_Clinic_Case, id=visit_id)
    return render(request,'Visit_Nurse_Service/Nurse_Pateiant_Visit.html',{'data':data })



# حفظ القياسات الحيوية

from .query_context_processors import get_user_requ

def Save_Vital_Singes_Visit_View(request):
    form =Vital_Signs_Form(request.POST)
    if request.method == "POST":
        id = request.POST.get('visit_no_id')
        visit_Case_id = Pateint_Visit_Clinic_Case.objects.get(id = id)
        pressure1 = request.POST.get('pressure_1')
        pressure2 = request.POST.get('pressure_2')
        Blood_pressure = pressure1 + "/" + pressure2
        if form.is_valid():
            Vital_Signs_form = form.save(commit=False)
            Vital_Signs_form.visit_Case = visit_Case_id
            Vital_Signs_form.ins_user_code = request.user
            Vital_Signs_form.patiant_no = visit_Case_id.Patiant_No
            Vital_Signs_form.Blood_pressure = Blood_pressure
            Vital_Signs_form.status = True
            visit_Case_id.Vital_Signs_Status = True
            visit_Case_id.save()
            Vital_Signs_form.save()
            return redirect('Nurse:Home') 





@login_required(login_url='login')
@His_decorators('Nrs_Clinic' , 'Dr_Clinic')
def Nurse_station_Patiant_Order_update(request, id):  #this function is called when update data
    data = Patiant_Visit_Order.objects.get(id=id)
    form = Patiant_Visit_Ruuselt_Order_Form(request.POST,request.FILES,instance = data)
    if form.is_valid():
        Order_Form = form.save(commit=False)
        Order_Form.Nurse_Result_Time = timezone.now()
        Order_Form.order_status = True
        form.save()
        return redirect('Nurse:Home')
    else:
        return redirect('Nurse:Home')




       
from xhtml2pdf import pisa
from django.template.loader import get_template

def Nurse_station_Patiant_pdf(request ,id):
	pdf = Patiant_Visit_Order.objects.get(id = id)
	template_path = 'Visit_Nurse_Service/pdf.html'
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


def Nurse_Admission_order_pdf(request ,id):
	pdf = Patient_Admission_Order.objects.get(id = id)
	template_path = 'Visit_Nurse_Service/pdf.html'
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
