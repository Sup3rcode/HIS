from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Patient_Files.models import *
from App_Home.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
today = timezone.now

# جدول حالة الدخول
class Patiant_Mode(models.Model):
    Mode_Name = models.CharField( max_length=21,blank=True,null=True)
    def __str__(self):
        return  str(self.Mode_Name)
    class Meta:
        db_table = 'Patiant_Mode'

# تسجيل زيارة 

class Pateint_Visit(models.Model):
    Reception = (
            ('OPD', 'OPD'),
        ('ER', 'ER'),
        )
    Reception = models.CharField(max_length=190, null=False , blank=False, choices=Reception , default='ER')
    Patiant_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Patiant')
    Patiant_Mode = models.ForeignKey(Patiant_Mode , on_delete=models.CASCADE , related_name='mod')
    Clinic_Name = models.ForeignKey(Clinic_List , on_delete=models.CASCADE ,related_name="Clinic_Name_%(class)s_objects")
    Visit_Date = models.DateTimeField(auto_now_add=True)
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  
    is_admission = models.BooleanField(default=False)
    admission_from_visit_case_id = models.CharField( max_length=100,blank=True,null=True)
    is_Close = models.BooleanField(default=False)
    Closed_Date = models.DateField(blank=True, null=True)
    Close_By_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="Close_By_%(class)s_objects") 
    Close_Details = models.CharField( max_length=100,blank=True,null=True)
    
    def __str__(self):
        return  str(self.id)
    class Meta:
        db_table = 'Patient_Visit'
    
  