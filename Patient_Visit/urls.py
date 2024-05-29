from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Patient_Visit'
urlpatterns = [
   path('', views.Patient_Visit_Home , name = "home"),
   path('last-24h/', views.Last_Patiant_24H , name = "Last_Patiant_24H"),
   path('validate_Visit/', views.validate_Visit, name="validate_Visit"),
   path('Send_Pateiant_To_Clinic/', views.Send_Pateiant_To_Clinic, name='Send_Pateiant_To_Clinic'),
   #### Transfer #### Transfer_Pateiant_To_Clinic
   path('Transfer_Pateiant_To_Clinic/', views.Transfer_Pateiant_To_Clinic, name='Transfer_Pateiant_To_Clinic'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)