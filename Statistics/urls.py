from django.urls import path
from .views.clinic_views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Statistics'
urlpatterns = [
   path('', index , name = "index"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)