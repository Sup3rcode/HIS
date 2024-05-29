from django.contrib import admin

from .models import *
# Register your models here.
apps_models = (Clinic_List    , )

admin.site.register(apps_models)
