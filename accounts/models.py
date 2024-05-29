from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Patient_Files.models import Nationality
from django.conf import settings

class Hospital_list(models.Model):
    Hospital_Name = models.CharField(blank=True,max_length=200 ,null=True , verbose_name='Hospital Name')
    Cloud_1 = models.CharField(blank=True,max_length=200 ,null=True , verbose_name='Cloud Site Primary')
    Cloud_2 = models.CharField(blank=True,max_length=200 ,null=True , verbose_name='Cloud Site Scandry')
    
    def __str__(self):
         return self.Hospital_Name

    class Meta:
        verbose_name_plural = "Hospital list"




class Role_list(models.Model):
    Role_Name = models.CharField(blank=True,max_length=200 ,null=True )
    user = models.ManyToManyField(User, related_name='role')
    
    
    def __str__(self):
         return self.Role_Name

#جدول الأقسام
class DEPARTEMENT(models.Model):
    DEPARTEMENT_Name = models.CharField(blank=True,max_length=200 ,null=True)
    def __str__(self):
         return self.DEPARTEMENT_Name

    class Meta:
        db_table = 'Hospital_DEPARTEMENTs'
#جدول التخصصات
class job_catogery(models.Model):
    job_catogery = models.CharField(blank=True,max_length=200 ,null=True)
    def __str__(self):
         return self.job_catogery
    class Meta:
        db_table = 'job_catogery'

class Employee_Type(models.Model):
    Employee_Type_List = (
        ('Doctor','Doctor'),
        ('Nurse','Nurse'),
        ('Nurse','Xray'),
        ('Radiology','Radiology'),
        ('Medecal Report','Medecal Report'),
        ('Medecal Record','Medecal Record') ,
        ('Reception','Reception')
      
    )
    Employee_Type =  models.CharField(verbose_name ="Employee_Type" ,max_length=200, null=True,choices=Employee_Type_List)
    
    def __str__(self):
         return self.Employee_Type
    class Meta:
        db_table = 'Employee_Type'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = (
        ('Male','Male'),
        ('Female','Female')
      
    )


    gender =  models.CharField(verbose_name ="Gender" ,max_length=200, null=True,choices=gender)
    job_number = models.CharField(null=True, blank=True , max_length=10)
    ID_number = models.CharField(null=True, blank=True , max_length=15)
    Employee_Type = models.ForeignKey(Employee_Type, null=True, on_delete=models.SET_NULL, related_name = 'Employee_Types')
    jobcatogery = models.ForeignKey(job_catogery, null=True, on_delete=models.SET_NULL, related_name = 'jobcatogery')
    Nationlity = models.ForeignKey(Nationality, null=True, on_delete=models.SET_NULL, related_name = 'NationalityIS')
    DEPARTEMNTS = models.ForeignKey(DEPARTEMENT, null=True, on_delete=models.SET_NULL, related_name = 'DEPARTEMENTIS')
    Active = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

