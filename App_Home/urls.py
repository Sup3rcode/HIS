from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'App_Home'
urlpatterns = [
   path('', views.index , name = "index"),
   path('11/', views.my_view , name = "my_view"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)