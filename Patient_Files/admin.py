from django.contrib import admin

# Register your models here.
from .models import *

class Archives_Patient_Files_ScannerAdmin(admin.ModelAdmin):
    exclude = ('Patiant_No',) 
admin.site.register(Archives_Patient_Files_Scanner , Archives_Patient_Files_ScannerAdmin)





class Patiant_File_NOAdmin(admin.ModelAdmin):
    
    
    list_display = ['patiant_no' , 'ar_patiant_name', 'en_patiant_name' , 'gender'  , 'birth_date' , 'nationalty']

admin.site.register(Patiant_File_NO, Patiant_File_NOAdmin)