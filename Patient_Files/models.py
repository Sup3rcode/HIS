from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


def Patient_Files_ID_Images(instance,filename):
    today = instance.en_patiant_name + '-' + instance.ar_patiant_name

    return "Medecal_Record/Archive_Patient_Files/%s/%s.jpeg"%(instance.patiant_no ,today)




# جدول الجنسيات
class Nationality(models.Model):  
    country_code = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    country_desc = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    area_code = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.
    male_nationality_desc = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    female_nationality_desc = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    country_e_desc = models.CharField(max_length=23, blank=True, null=True)  # Field name made lowercase.
    nationality_e_desc = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
         return str(self.country_desc) + '  - ' + str(self.nationality_e_desc)

    class Meta:
        db_table = 'Nationality'
gender = (
        ('1','Male'),
        ('2','Female')
      
    )


# جدول معلومات المريض
class Patiant_File_NO(models.Model):
   
    registration_date = models.DateField(auto_now_add=True)  
    patiant_no = models.IntegerField()  
    ar_patiant_name = models.CharField(max_length=200 , blank=True, null=True)  
    en_patiant_name = models.CharField(max_length=200 , blank=True, null=True)  
    birth_date = models.DateField(blank=False, null=False)  
    gender =  models.CharField(max_length=200, null=True,choices=gender)
    nationalty = models.ForeignKey(Nationality, on_delete=models.DO_NOTHING, blank=True, null=True )
    social_number = models.CharField( max_length=200 , blank=True, null=True , unique=False )  
    address = models.CharField(max_length=200,blank=True, null=True)  
    mobile_no = models.IntegerField(blank=True, null=False , unique=False)  
    mother_name = models.CharField(max_length=200,blank=True, null=True)  
    mother_med_no = models.IntegerField(blank=True, null=True)  
    patiant_no_form = models.CharField(max_length=200,blank=True, null=True)  
    smok_status = models.CharField(max_length=200,blank=True, null=True)  
    ins_user_code = models.ForeignKey(User, on_delete=models.DO_NOTHING,  related_name='Patiant_File_NO_insert_user_code' ,null=True, blank=True)
    ins_user_date = models.DateField(auto_now_add=True ,blank=True, null=True)  
    upd_user_code = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    upd_user_date = models.DateField( blank=True, null=True)  
    mother_id = models.IntegerField(blank=True, null=True)
    ID_image = models.ImageField(upload_to=Patient_Files_ID_Images , blank=True, null=True)
    class Meta:
        db_table = 'Patiant_File_NO'
    def __str__(self):
         return str(self.patiant_no)
    def save(self, *args, **kwargs):
        date_id = self.registration_date
        if date_id == None :
            self.registration_date = datetime.now() 
            return super().save(*args, **kwargs)

import random



def Archives_Patient_Files(instance,filename):
    today = random.randint(1000000000000, 9999999999999)

    return "Medecal_Record/Archive_Patient_Files/%s/%s.jpeg"%(instance.Patiant_No ,today)






class Archives_Patient_Files_Scanner(models.Model):
    Patiant_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Archive_Patient_Files')
    image = models.ImageField(upload_to=Archives_Patient_Files)
    By_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    Scan_Date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  
