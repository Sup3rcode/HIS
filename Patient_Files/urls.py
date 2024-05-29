

from unicodedata import name
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from . import views
app_name = 'Patient_Files'

urlpatterns = [
    path('get_patiant_Data/', views.get_patiant_Data, name='get_patiant_Data'),
    path("medecal_report/", index_js, name="medecal_report"),
    path("Save_Scan_Images/", Save_Scan_Images, name="Save_Scan_Images"),
    path('validate_saudi_id/', views.validate_saudi_id, name='validate_saudi_id'),
    path('validate_patient_pdf_file_id/', views.validate_patient_pdf_file_id, name='validate_patient_pdf_file_id'),
    path('validate_social_number/', views.validate_social_number, name="validate_social_number"),
    path('ar_convert/', views.ar_convert, name="ar_convert"),
    path('pdf/<int:id>', views.Patiant_file_list_pdf, name='Patiant_file_list_pdf'),
    path('Create_new_FILE/', views.Create_PatiantFile, name='Create_new_FILE'),
    path('get_files/', views.get_files, name='get_files'),
    path('pateint/pdf/<int:id>', views.patient_pdf_up, name='patient_pdf_up'),
]
router = DefaultRouter()

router.register("api/File_NO_list", Patiant_File_NOViewSet, basename="File_NO_list")
urlpatterns += router.urls