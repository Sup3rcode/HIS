from django.contrib import admin
from .models import *
# Register your models here.
modler = (Transfer_Tybe    , Admission_Room)

admin.site.register(modler)
class Patient_Admission_Order_Nurse_NoteAdmin(admin.ModelAdmin):
    exclude = ('patiant_no',)
   

class Admission_Room_BedAdmin(admin.ModelAdmin):
    exclude = ('Patient_No',)
   
 
    
admin.site.register(Admission_Room_Bed , Admission_Room_BedAdmin)


admin.site.register( Admission_Section)
admin.site.register( Transfer_Patient_To_ِِanother_Section)

class Patient_Admission_CaseAdmin(admin.ModelAdmin):
    exclude = ('patiant_no',)
admin.site.register(Patient_Admission_Case , Patient_Admission_CaseAdmin)


class Patient_Admission_Case_Visit_SectionAdmin(admin.ModelAdmin):
    exclude = ('Patient_No',)
admin.site.register(Patient_Admission_Case_Visit_Section , Patient_Admission_Case_Visit_SectionAdmin)