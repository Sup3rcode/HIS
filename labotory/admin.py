from django.contrib import admin

# Register your models here.
from .models import *


test_tube = ( Labotory_Tube_List , Tube_Barcode_Number  , Specimens_Arrival_Visit)


admin.site.register(test_tube)


class Labotory_TestAdmin(admin.ModelAdmin):
    list_filter = ('test_name','test_tybe')
admin.site.register(Labotory_Test , Labotory_TestAdmin)

