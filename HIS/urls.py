from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('clsr/', admin.site.urls),

    path('', include('accounts.url')),
    path('', include('App_Home.urls')),
    path('files/', include('Patient_Files.urls')),
    path('Visit/', include('Patient_Visit.urls')),
    path('Nurse/', include('Nurse.urls')),
    path('Patient-Clinic-list/', include('Visit_Clinic.urls')),
    path('lab/', include('labotory.urls')),
    path('Patient_Admission', include('Admission.urls')),
    path('Statistics/', include('Statistics.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import handler404
import App_Home.views
handler404 = App_Home.views.error_404


