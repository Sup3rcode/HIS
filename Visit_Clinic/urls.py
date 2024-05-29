from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Visit_Clinic'
urlpatterns = [
   path('', views.index , name = "index"),
   path('Get_Visit_By_Clinic_Name', views.Get_Visit_By_Clinic_Name, name='Get_Visit_By_Clinic_Name'),
   path('Patiant_Visit_Case_View/<int:visit_id>/', views.Patiant_Visit_Case_View , name = "Patiant_Visit_Case_View"),
   path('Patiant_Visit_Case_View/2/<int:visit_id>/', views.Patiant_Visit_Case_View2 , name = "Patiant_Visit_Case_View2"),
   path('Patiant_Visit_Case_Save/', views.Patiant_Visit_Case_Save , name = "Patiant_Visit_Case_Save"),
   path('Patiant_Visit_Order_Save/', views.Patiant_Visit_Order_Save , name = "Patiant_Case_Order_Save"),

   path('Patiant_Case_Admission_Save/', views.Patiant_Case_Admission_Save , name = "Patiant_Case_Admission_Save"),

   ########### Xray ###############
   path('xray_order_list_view/', views.xray_order_list_view , name = "xray_order_list_view"),
   path('xray_order_list_view2/', views.xray_order_list_view2 , name = "xray_order_list_view2"),
   path('Patiant_Visit_xray_Save/', views.Patiant_Visit_Xray_Save , name = "Patiant_Case_Xray_Save"),
   path('xray_report_view/<int:visit_id>/', views.xray_report_view , name = "xray_report_view"),
   path('show_report_xray/', views.show_report_xray , name = "show_report_xray"),
   path('xrat-24h/', views.xray_visit_list_view , name = "xray_visit_list"),
   path('get_visit/', views.get_visit , name = "get_visit"),
   path('xray_Reception_Send_To_Report/', views.xray_Reception_Send_To_Report , name = "xray_Reception_Send_To_Report"),
   path('Report_Xray_Save/', views.Report_Xray_Save , name = "Report_Xray_Save"),


   ############## Close ###########
      path('Visit_Close/', views.Visit_Close , name = "Visit_Close"),

      path('cheack_visit_sc/', views.cheack_visit_sc , name = "cheack_visit_sc"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)