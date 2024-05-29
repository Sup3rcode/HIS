from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Admission'
urlpatterns = [
   path('load_Bed/', views.load_Bed , name = "load_Bed"),
   path('Patient_Admission_Transfer_View/', views.Patient_Admission_Transfer_View , name = "Patient_Admission_Transfer_View"),
   path('Patient_Admission_Visited_Details_view/<int:visit_id>/', views.Patient_Admission_Visited_Details_view , name = "Patient_Admission_Visited_Details_view"),
   path('Reject_to_Section_view/', views.Reject_to_Section_view , name = "Reject_to_Section_view"),
   path('Assgin_Pateont_To_Bed_view/', views.Assgin_Pateont_To_Bed_view , name = "Assgin_Pateont_To_Bed_view"),
   path('Patient_Accepted_Section_Status_view/', views.Patient_Accepted_Section_Status_view , name = "Patient_Accepted_Section_Status_view"),
   path('Patient_Accepted_Transfer/', views.Patient_Accepted_Transfer , name = "Patient_Accepted_Transfer"),
   path('get_visit/', views.get_visit , name = "get_visit"),
   path('admission_Case_Xray_Save/', views.Patiant_Visit_Xray_Save , name = "admission_Case_Xray_Save"),
   
   ## Nurse_Visit_Section_Admission
   path('Nurse_Visit_Section_Admission/<int:Section_id>/', views.Nurse_Visit_Section_Admission , name = "Nurse_Visit_Section_Admission"),
   path('Admission_Order_Nurse_Note_View/', views.Admission_Nurse_Note_View , name = "Admission_Order_Nurse_Note_View"),
   path('Nurse_Note_Pdf/<int:id>', views.Nurse_Note_Pdf, name='Nurse_Note_Pdf'),
   path('Patient_Admission_Vital_Signs_View/', views.Patient_Admission_Vital_Signs_View , name = "Patient_Admission_Vital_Signs_View"),
   path('Patient_Befor_Admission_Nurse_View/<int:id>/', views.Patient_Befor_Admission_Nurse_View , name = "Patient_Befor_Admission_Nurse_View"),
   path('Nurse_Admission_Order_update/<int:id>/', views.Nurse_Admission_Order_update , name = "Nurse_Admission_Order_update"),

   # Discharge
   path('Patient_Admission_Doctor_Discharge_View/', views.Patient_Admission_Doctor_Discharge_View , name = "Patient_Admission_Doctor_Discharge_View"),
   
   #  Doctor_Visit
   path('Doctor_Visit_Section_Admission/<int:Section_id>/', views.Doctor_Visit_Section_Admission , name = "Doctor_Visit_Section_Admission"),
   path('Patient_Admission_Doctor_Order_View/', views.Patient_Admission_Doctor_Order_View , name = "Patient_Admission_Doctor_Order_View"),
   path('Patient_Admission_Doctor_Visit_Case_View/', views.Patient_Admission_Doctor_Visit_Case_View , name = "Patient_Admission_Doctor_Visit_Case_View"),
   path('Doctor_Patient_Admission_Visited_Details_view/<int:visit_id>/', views.Doctor_Patient_Admission_Visited_Details_view , name = "Doctor_Patient_Admission_Visited_Details_view"),
   path('Reject_to_doctor_view/', views.Reject_to_doctor_view , name = "Reject_to_doctor_view"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)