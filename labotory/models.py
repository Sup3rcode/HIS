from hashlib import new
from django.db import models
from App_Home.models import *
from Visit_Clinic.models import *
from Patient_Visit.models import *
from Admission.models import *
from io import BytesIO
from django.core.files import File
# Create your models here.
import random 
from django.utils.text import slugify 
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
import barcode
from barcode.writer import ImageWriter
from django.conf import settings

def number_barcode_function():
    test_barcode_Number =  random.randint(1000000000000, 9999999999999)
    return test_barcode_Number
from Admission.models import *
def last_number_barcode_function():
    barcode_Number =  Labotory_Tube_List.objects.last().Tube_num
    return barcode_Number

class Labotory_Test(models.Model):  
    test_name = models.CharField(max_length=50 ,blank=True, null=True)
    test_tybe = models.CharField(max_length=50 ,blank=True, null=True)

    def __str__(self):
         return self.test_name

    class Meta:
        db_table = 'Labotory_Test'


class Labotory_Tube_List(models.Model):
    Tube_Name = models.CharField(max_length=50 ,blank=True, null=True , )  
    Tube_num = models.CharField(max_length=50 ,blank=True, null=True )
    def __str__(self):
         return self.Tube_num
    def save(self, *args, **kwargs):
        self.Tube_num = number_barcode_function()
        return super().save(*args, **kwargs)
    class Meta:
        db_table = 'Labotory_Tube_List'


class Tube_Barcode_Number(models.Model):
    Tube_Test_Tybe = models.CharField(max_length=50 ,blank=True, null=True , )  
    Tube_Number = models.CharField(max_length=50 ,blank=True, null=True )
    Tube_Visit_Number = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE , related_name='Tube_Visit_Number')
    def __str__(self):
         return self.Tube_Number
    class Meta:
        db_table = 'Tube_Barcode_Number'



class Specimens_Arrival_Visit(models.Model):
    Barcode_Number = models.ForeignKey(Tube_Barcode_Number , on_delete=models.CASCADE , related_name='Barcode_Number')
    Specimens_Visit_Number = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE , related_name='Specimens_Visit_Number')
    Tube_Test_Name = models.ForeignKey(Labotory_Test , on_delete=models.CASCADE , related_name='Tube_Test_Name', null=True, blank=True)
    Tube_Test_Name2 = models.CharField(max_length=50 ,blank=True, null=True )
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Pateiant_tube_Visit', null=True, blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    barcode_img = models.ImageField(upload_to='images/Barcode', blank=True)
    is_Done = models.BooleanField(default=False)
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  
    
    class Meta:
        db_table = 'Specimens_Arrival_Visit'
    def __str__(self):
        return  str(self.patiant_no)
    def save(self, *args, **kwargs):
        bar_num = Tube_Barcode_Number.objects.filter(Tube_Number = self.Barcode_Number)
        img_number = str(self.Barcode_Number)
        EAN = barcode.get_barcode_class('code39')
        ean = EAN(img_number, writer=ImageWriter() , add_checksum=False)
        buffer = BytesIO()
        ean.write(buffer , options = {'text_distance': 4.0, 'module_height': 4.0, 'center_text' : True , 'font_size': 8, 'quiet_zone': 1.0, 'module_width': 0.15})
        self.barcode_img.save(f'{self.id}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)




class test_save(models.Model):
    test_Visit_Number = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE , related_name='test_Visit_Number')
    test_patient_no= models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='test_patient_no')
    def __str__(self):
         return str(self.test_patient_no)
    def save(self, *args, **kwargs):
        tsa = Patiant_File_NO.objects.get(id = self.test_Visit_Number.patiant_no.id)
        self.test_patient_no = tsa
        return super().save(*args, **kwargs)




#-----------------// Admission //----------##


class Tube_Barcode_Number_admission(models.Model):
    Tube_Test_Tybe = models.CharField(max_length=50 ,blank=True, null=True , )  
    Tube_Number = models.CharField(max_length=50 ,blank=True, null=True )
    Tube_Visit_Number = models.ForeignKey(Patient_Admission_Case_Visit_Section , on_delete=models.CASCADE , related_name='Tube_Visit_addmiss')
    def __str__(self):
         return self.Tube_Number
    class Meta:
        db_table = 'Tube_Barcode_Number_admission'



class Specimens_Arrival_admission(models.Model):
    Barcode_Number = models.ForeignKey(Tube_Barcode_Number_admission , on_delete=models.CASCADE , related_name="Barcode%(class)s_objects")
    Admission_Visit_id = models.ForeignKey(Patient_Admission_Case_Visit_Section , on_delete=models.CASCADE , related_name="Section_%(class)s_objects")
    Tube_Test_Name = models.ForeignKey(Labotory_Test , on_delete=models.CASCADE , related_name="Tube%(class)s_objects", null=True, blank=True)
    Tube_Test_Name2 = models.CharField(max_length=50 ,blank=True, null=True )
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name="Patient_%(class)s_objects", null=True, blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    barcode_img = models.ImageField(upload_to='images/Barcode', blank=True)
    is_Done = models.BooleanField(default=False)
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  
    
    class Meta:
        db_table = 'Specimens_Arrival_admission'
    def __str__(self):
        return  str(self.patiant_no)
    def save(self, *args, **kwargs):
        bar_num = Tube_Barcode_Number.objects.filter(Tube_Number = self.Barcode_Number)
        img_number = str(self.Barcode_Number)
        EAN = barcode.get_barcode_class('code39')
        ean = EAN(img_number, writer=ImageWriter() , add_checksum=False)
        buffer = BytesIO()
        ean.write(buffer , options = {'text_distance': 4.0, 'module_height': 4.0, 'center_text' : True , 'font_size': 8, 'quiet_zone': 1.0, 'module_width': 0.15})
        self.barcode_img.save(f'{self.id}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

