from django.contrib import admin

from .models import *
from Visit_Clinic.models import Pateint_Visit_Clinic_Case

class Pateint_Visit_Clinic_CaseAdmin(admin.ModelAdmin):
    exclude = ('Patiant_No',) 
admin.site.register(Pateint_Visit_Clinic_Case , Pateint_Visit_Clinic_CaseAdmin)





class Pateint_VisitAdmin(admin.ModelAdmin):
    exclude = ('Patiant_No',) 
admin.site.register(Pateint_Visit , Pateint_VisitAdmin)