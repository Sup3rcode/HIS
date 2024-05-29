from django.shortcuts import render
from .models import *
from django.db.models import Q
from .serializers import  Patiant_File_NOSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from luhn_validator import validate
from django.http import JsonResponse , HttpResponse
from .ar_convert import *
from .forms import *
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from accounts.decorators import His_decorators




@login_required(login_url='login')
@His_decorators('Patient_Files' )
def index_js(request):
    return render(request, "Patient_Files/medecal_report.html")

def get_patiant_Data(request):
    if request.method == "GET":
        theid = request.GET.get('term')
        ER_Search  = Patiant_File_NO.objects.filter(
    Q(ar_patiant_name__icontains=theid) | Q(social_number__icontains=theid))[:10]
        return JsonResponse(list(ER_Search.values('id','patiant_no','ar_patiant_name')), safe=False)

# التحقق من رقم الهوية
def validate_saudi_id(request):
    saudi_id = request.GET.get('social_number', None)
    data = {
  
        'is_taken':     validate(saudi_id)
    }
    if data['is_taken'] == False:
        data['error_message'] = 'رقم الهوية أو الإقامة غير صحيح '
    return JsonResponse(data)


def validate_patient_pdf_file_id(request):
    theid = request.GET.get('get_id')
    data = {
  
        'is_taken':     Archives_Patient_Files_Scanner.objects.filter(Patiant_No__id = theid).exists()
    }
    if data['is_taken'] == False:
        data['error_message'] = 'لايوجد ملفات مؤرشفة '
    return JsonResponse(data)


# التحقق من وجود ملف سابق
def validate_social_number(request):
    social_number = request.GET.get('social_number', None)
    data = {'is_exists':     Patiant_File_NO.objects.filter(social_number=social_number).exists()}
    if data['is_exists'] == True:
        data['error_message'] = 'this number already exists & رقم الهوية مسجل مسبقاً'
    return JsonResponse(data)



def ar_convert(request):
    ar_txt = request.GET.get('ar_name')
    data = {'en_txt':transString(ar_txt , 0)}
    return JsonResponse(data)




@login_required(login_url='login')
@His_decorators('Patient_Files' , 'Reception' )
def Create_PatiantFile(request):
    
    if request.method == 'POST':

        form = Patiant_File_NO_Form(request.POST)
        last_id = Patiant_File_NO.objects.last().patiant_no
        last_pa = last_id +1
        if form.is_valid():
            Patiant_create = form.save(commit=False)
            Patiant_create.patiant_no = last_pa 
            
            Patiant_create.save()
        data = {'pateiant_no': last_pa}
        return JsonResponse(data)


def get_files(request):
    if request.method == "GET":
        theid = request.GET.get('get_id')
        data  = data= Archives_Patient_Files_Scanner.objects.filter(Patiant_No__id = theid)
        #data  = Pateint_Visit_Clinic_Case.objects.filter(Clinic_Name__id__icontains=theid , is_admission = False).order_by('-id')
        data1 = render_to_string('Clinic_Visit/Clinic_List_2.html',{'data': data},request=request)
        return JsonResponse(data1 , safe=False)

@login_required(login_url='login')
@His_decorators('Patient_Files' , 'Reception' )   
def Save_Scan_Images(request):
        if request.method == 'POST':
            upload_file = request.FILES.get('blob')
            File_No = request.POST.get('File_id')
            user_id= User.objects.get(id=request.user.id)
            _Patient_No = Patiant_File_NO.objects.get(id=File_No)
            Archives_Patient_Files_Scanner.objects.create(
                Patiant_No = _Patient_No ,
                image=upload_file,
                By_User=user_id,
        )
        data= Archives_Patient_Files_Scanner.objects.all().values()
        
        
        return JsonResponse(list(data) , safe=False)
   



from xhtml2pdf import pisa
from django.template.loader import get_template
@login_required(login_url='login')
@His_decorators('Patient_Files' , 'Reception' )
def Patiant_file_list_pdf(request ,id):
	pdf = Archives_Patient_Files_Scanner.objects.filter(Patiant_No__id = id)
	template_path = 'Patient_Files/pdf.html'
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


def Patiant_pdf(request ,id):
	pdf = Archives_Patient_Files_Scanner.objects.filter(Patiant_No__id = id)
	Patient_No_id = Patiant_File_NO.objects.get(id=pdf.Patiant_No.id)
    
	template_path = 'Patient_Files/pdf.html'
	context = {'pdf':pdf , 'emp':Patient_No_id}
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
@His_decorators('Patient_Files' , 'Reception' )
def patient_pdf_up(request ,id):
	
	pdf = Archives_Patient_Files_Scanner.objects.filter(Patiant_No__id = id)
	emp = Patiant_File_NO.objects.get(id=id)
	template_path = 'Patient_Files/scanner/pdf.html'
	context = {'pdf':pdf , 'emp':emp}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(html, dest=response)
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

class Patiant_File_NOViewSet(viewsets.ModelViewSet):
   
    serializer_class = Patiant_File_NOSerializer
    queryset = Patiant_File_NO.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['ar_patiant_name', 'mobile_no', "social_number"]
    search_fields = ['ar_patiant_name', 'mobile_no', "social_number"]
    ordering_fields = '__all__'

