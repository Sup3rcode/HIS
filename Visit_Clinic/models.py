from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Patient_Files.models import *  
from Patient_Visit.models import *
from App_Home.models import *
import os
from uuid import uuid4
from django.urls import reverse

# -------------// models choices //---------------#

import random
def Patient_Visit_Order_Images(instance,filename):
    visit_id = instance.visit_Case.id
    Patient_No = instance.patiant_no.patiant_no
    random_num = random.randint(1000000000000, 9999999999999)
    return "Patient_Visit/Visit_Order/%s/%s/%s.jpeg"%(visit_id , Patient_No ,random_num)


# جدول نوع الأشعة
class Xray_type(models.Model):
    Xray_type = models.CharField( max_length=21,blank=True,null=True)
    def __str__(self):
        return  str(self.Xray_type)
    class Meta:
        db_table = 'Xray_type'


# مكان الأشعة بالجسم
class Xray_Site(models.Model):
    Xray_Site = models.CharField( max_length=21,blank=True,null=True)
    def __str__(self):
        return  str(self.Xray_Site)
    class Meta:
        db_table = 'Xray_Site'


# -------------//end  models choices //---------------#


#################################################################     
# تسجيل الزيارات بالعيادة
class Pateint_Visit_Clinic_Case(models.Model):
    Visit_id = models.ForeignKey(Pateint_Visit , on_delete=models.CASCADE ,related_name='Visits')
    Patiant_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE )
    Visit_Type = models.CharField( max_length=100,blank=True,null=True)
    Visit_Date = models.DateTimeField(auto_now_add=True)
    Vital_Signs_Status = models.BooleanField(default=False)
    Visit_Opened_status = models.BooleanField(default=False)
    Opened_Date = models.DateTimeField(blank=True, null=True)
    Open_By_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True ,related_name="Opened_By_%(class)s_objects")
    Clinic_Name = models.ForeignKey(Clinic_List , on_delete=models.CASCADE ,related_name="Pateint_Visit_Clinic_Name")
    is_Close = models.BooleanField(default=False)
    Closed_Date = models.DateTimeField(blank=True, null=True)
    Close_By_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True ,related_name="Close_By_%(class)s_objects")
    Close_Details = models.CharField( max_length=100,blank=True,null=True) 
    is_Transfer = models.BooleanField(default=False)
    Transfer_Date = models.DateTimeField(blank=True, null=True)
    Transfer_By_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="Transfer_By_%(class)s_objects") 
    Transfer_Details = models.CharField( max_length=100,blank=True,null=True)

    def __str__(self):
        return  str(self.id)
    class Meta:
        db_table = 'Pateint_Visit_Clinic_Case'
        ordering = ['-id']

    def get_Patient_Vital_url(self):
        return reverse('Nurse:Nurse_station_Patiant_Visit', args=[self.pk])
    
    def get_patient_visit_list(self):
        
        get_visit = Pateint_Visit_Clinic_Case.objects.filter(Patiant_No__id=self.Patiant_No.id)
        for i in get_visit :
            visit_history = Patiant_Visit_History.objects.filter(visit_Case__id = i.id)
            print(visit_history)
        
        context = {
           
            'get_visit':get_visit


          }
        return context
    

#################################################################
class BaseModel_clinic(models.Model):
    visit_Case = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE ,related_name="Visit_id_%(class)s_objects")
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE ,related_name="Patient_%(class)s_objects")
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE) 
    ins_user_date = models.DateTimeField(auto_now_add=True)  

    class Meta:
        abstract = True
   
#################################################################



#################################################################
# سجل تشخيص الزيارة
class Patiant_Visit_History(BaseModel_clinic):
    History =models.TextField(verbose_name='History & Physical' ,blank=True, null=True)
    Diagnosis=models.TextField(verbose_name='Diagnosis',blank=True, null=True)
    Examination=models.TextField(verbose_name='Examination',blank=True, null=True)
    Doctor_Note= models.TextField(verbose_name='Doctor Note',blank=True, null=True)
    
    class Meta:
        db_table = 'Patiant_Visit_History'
    def __str__(self):
         return str(self.visit_Case)

    def save(self, *args, **kwargs):
        patiant_no = Patiant_File_NO.objects.get(id = self.visit_Case.Patiant_No.id)
        self.patiant_no = patiant_no
        return super().save(*args, **kwargs)

#################################################################


#################################################################
 # إرسال الطلبات للتمرض   
class Patiant_Visit_Order(BaseModel_clinic):
    Dr_Order = models.CharField(max_length=100,blank=True,null=True)
    Nurse_Note=models.TextField(verbose_name='Nurse_Note')
    Nurse_Result_Time=models.DateTimeField(null=True, blank=True)
    order_status = models.BooleanField(default=False)
    Visit_Files = models.ImageField(upload_to=Patient_Visit_Order_Images, null=True, blank=True)

    class Meta:
        db_table = 'Patiant_Visit_Order'
    
    def save(self, *args, **kwargs):
        patiant_no = Patiant_File_NO.objects.get(id = self.visit_Case.Patiant_No.id)
        self.patiant_no = patiant_no
        return super().save(*args, **kwargs)
    def __str__(self):
         return str(self.visit_Case)

#################################################################



# طلب أشعة
class Patiant_Visit_Xray(BaseModel_clinic):
    Status = (
        ('Waiting Reception', 'Waiting Reception'),
        ('Waiting Report', 'Waiting Report'),
        ('Finish', 'Finish'),
    )
    Visit_History = models.ForeignKey(Patiant_Visit_History , on_delete=models.CASCADE )
    Xray_type = models.ForeignKey(Xray_type , on_delete=models.CASCADE , related_name='Xray_Type_Visit', null=True, blank=True)
    Xray_Site = models.ForeignKey(Xray_Site , on_delete=models.CASCADE , related_name='Xray_Site_Visit', null=True, blank=True)
    Status_Reception_time =models.DateTimeField(auto_now_add=True ,null=True, blank=True)  
    xray_status = models.CharField(max_length=20, choices=Status, default="Waiting Reception")
    class Meta:
        db_table = 'Patiant_Visit_Xray'
    def __str__(self):
        return  str(self.visit_Case)
    def save(self, *args, **kwargs):
        patiant_no = Patiant_File_NO.objects.get(id = self.visit_Case.Patiant_No.id)
        Visit_History = Patiant_Visit_History.objects.filter(visit_Case__id = self.visit_Case.id).last()
        self.Visit_History = Visit_History
        self.patiant_no = patiant_no
        return super().save(*args, **kwargs)



# تقرير الأشعة
class Patiant_Visit_Xray_Report(models.Model):
    Order_xray = models.ForeignKey(Patiant_Visit_Xray , on_delete=models.CASCADE , related_name='Order_xray')
    Report_details = models.TextField(blank=True,null=True , verbose_name='Report_details')
    Report_time=models.DateTimeField(null=True, blank=True)
    is_visit = models.BooleanField(default=False)
    visit_time=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return  str(self.id)
    class Meta:
        db_table = 'Patiant_Visit_Xray_Report'