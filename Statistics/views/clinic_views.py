from django.shortcuts import render , redirect
from Visit_Clinic.models import *
from django.db.models import Count
from Patient_Visit.models import *
from Ward.models import *
def index(request):
    ward = Admission_Section.objects.all()[:6]
    clinics = Clinic_List.objects.all()
    
    Visit_total = Clinic_List.objects.all()[:6]
    return render(request, 'Statistics/index.html' , {'Visit_total':Visit_total , 'ward':ward})