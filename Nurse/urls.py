from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Nurse'
urlpatterns = [
   path('', views.Home , name = "Home"),
   path('Nurse_station_Patiant_Visit/<int:visit_id>/', views.Nurse_station_Patiant_Visit , name = "Nurse_station_Patiant_Visit"),
   path('Save_Vital_Singes_Visit_View/', views.Save_Vital_Singes_Visit_View , name = "Save_Vital_Singes_Visit_View"),
   path('Nurse_station_Patiant_Order_update/<int:id>/', views.Nurse_station_Patiant_Order_update , name = "Nurse_station_Patiant_Order_update"),
   path('pdf/<int:id>', views.Nurse_station_Patiant_pdf, name='order_pdf'),
   path('Admission_order/<int:id>', views.Nurse_Admission_order_pdf, name='Nurse_Admission_order_pdf'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)