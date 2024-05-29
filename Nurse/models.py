from django.db import models
from Patient_Files.models import Patiant_File_NO
from Visit_Clinic.models import *
from django.contrib.auth.models import User
import os
from uuid import uuid4




def path_and_rename(instance, filename):
    upload_to = 'visit_Order'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

import random
def Patiant_Visit_Nurse_Note_Images(instance,filename):
    visit_id = instance.visit_Case.id
    Patient_No = instance.Patiant_No.en_patiant_name + '-' + instance.Patiant_No.ar_patiant_name
    random_num = random.randint(1000000000000, 9999999999999)
    return "Patient_Visit/Nurse_Note/%s/%s/%s/.jpeg"%(visit_id , Patient_No ,random_num)



# مودل الأب لخدمات التمريض
class BaseModel_Nurse(models.Model):
    visit_Case = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE ,related_name="Visit_id_%(class)s_objects")
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE ,related_name="Patient_%(class)s_objects")
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  

    class Meta:
        abstract = True


# القياسات الحيوية
class Visit_Vital_Signs(BaseModel_Nurse):
    Body_weight = models.FloatField(null=True)
    Height = models.FloatField(null=True)
    Temp = models.FloatField(null=True)
    Blood_pressure = models.CharField(max_length=21,blank=True,null=True)
    spo2 = models.CharField(max_length=21,blank=True,null=True , verbose_name='Spo2 ( % )')
    Resp_rate = models.IntegerField()
    Vital_Status = models.BooleanField(default=False)
    

    def get_last_Pateint_Visit_True(self):
        return Pateint_Visit_Clinic_Case.objects.filter(Visit_status=True)
    class Meta:
        db_table = 'Visit_Vital_Signs'
    def __str__(self):
        return  str(self.visit_Case)
  
    def save(self, *args, **kwargs):
        patiant_no = Patiant_File_NO.objects.get(id = self.visit_Case.Patiant_No.id)
        self.patiant_no = patiant_no
        return super().save(*args, **kwargs)
    def __str__(self):
         return str(self.visit_Case)



 
class Patiant_Visit_Nurse_Note(BaseModel_Nurse):
    Nurse_Note=models.TextField(verbose_name='Patiant_Nurse_Note')
    Note_Files = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Patiant_Visit_Nurse_Note'
    
    def save(self, *args, **kwargs):
        patiant_no = Patiant_File_NO.objects.get(id = self.visit_Case.patiant_no.id)
        self.patiant_no = patiant_no
        return super().save(*args, **kwargs)
    def __str__(self):
         return str(self.visit_Case)


