from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *
from Visit_Clinic.models import *



@receiver(post_save, sender=Pateint_Visit) 
def create_new_visit(sender, instance, created, **kwargs):
    if created:
        id_case = Pateint_Visit.objects.get(id=instance.id)
        _Clinic = Clinic_List.objects.get(id=instance.Clinic_Name.id)
        _Patient_No = Patiant_File_NO.objects.get(id=instance.Patiant_No.id)
        Pateint_Visit_Clinic_Case.objects.create(Visit_id=id_case , Patiant_No = _Patient_No , Clinic_Name = _Clinic)
post_save.connect(create_new_visit, sender=Pateint_Visit)