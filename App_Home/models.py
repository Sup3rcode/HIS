from django.db import models
from django.contrib.auth.models import User



# جدول العيادات
class Clinic_List(models.Model):
    Clinic_Name = models.CharField( max_length=21,blank=False,null=True)
    Clinic_Ty = (
            ('OPD', 'OPD'),
        ('ER', 'ER'),
        )
    Clinic_Tybe = models.CharField(max_length=190, null=False , blank=False, choices=Clinic_Ty)
    Clinic_status = models.BooleanField(default=False)
    User_Access = models.ManyToManyField(User, blank=True,) 
    def __str__(self):
        return  str(self.Clinic_Name)
    class Meta:
        db_table = 'Clinic_List'
 