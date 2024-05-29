from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'labotory'
urlpatterns = [
   path('', views.index , name = "index"),
   path('Barcode_Search/', views.Barcode_Search , name = "Barcode_Search"),
   path('lab/', views.index2 , name = "index2"),
   path('lis/', views.visit_lab_order_list , name = "visit_lab_order_list"),
   path('get_Labotory_Tybe/', views.get_Labotory_Tybe, name='get_Labotory_Tybe'),
   path('get_Labotory_Tybe_Admission_Case/', views.get_Labotory_Tybe_Admission_Case, name='get_Labotory_Tybe_Admission_Case'),
   path('Specimens_Arrival_View/', views.Specimens_Arrival_View, name='Specimens_Arrival_View'),
   path('Specimens_Reception_Send_To_lab/', views.Specimens_Reception_Send_To_lab, name='Specimens_Reception_Send_To_lab'),
   path('Admission_Send_Order_to_lab/', views.Admission_Send_Order_to_lab , name = "Admission_Send_Order_to_lab"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)