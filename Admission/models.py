from django.db import models
from Ward.models import *
from Patient_Visit.models import *
from Patient_Files.models import *
from django.contrib.auth.models import User
from Visit_Clinic.models import *



import random

import random
def Patient_Admission_Order_Images(instance,filename):
    visit_id = instance.Admission_visit_Case.id
    Patient_No = instance.patiant_no.patiant_no
    random_num = random.randint(1000000000000, 9999999999999)
    return "Patient_Visit/Admission_Order/%s/%s/%s.jpeg"%(visit_id , Patient_No ,random_num)



# مودل الأب - دخول المريض لقسم التنويم
class Patient_Admission_Case(models.Model):
    Visit_Case = models.ForeignKey(Pateint_Visit , on_delete=models.CASCADE  )
    Visit_Clinic = models.ForeignKey(Pateint_Visit_Clinic_Case , on_delete=models.CASCADE  )
    Admission_Section = models.ForeignKey(Admission_Section , on_delete=models.CASCADE , related_name="Patient_Visit_Section_Ward" )
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE ,related_name="Patient_%(class)s_objects")
    Admission_Description = models.TextField(verbose_name='Admission_Description' ,blank=True,null=True )
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)
    Start_Admission_Date = models.DateTimeField(blank=True,null=True )
    End_Admission_Date = models.DateTimeField(blank=True,null=True )
    Discharge_status = models.BooleanField(default=False)
    Discharge_Date = models.DateTimeField(blank=True,null=True )
    Visit_Case_is_Closed = models.BooleanField(default=False)
    Discharge_OF_Section_ID = models.CharField( max_length=200,blank=True,null=True )

#self.request.user
    def __str__(self):
        return str(self.patiant_no) + '  - ' + str(self.Admission_Section)
    
    class Meta:
        unique_together = (('Visit_Case', 'Visit_Clinic'),)
        db_table = 'Patient_Admission_Case'



# مودل الإبن - فترة بقاء المريض بقسم التويم
class Patient_Admission_Case_Visit_Section(models.Model):
    Admission_Case_id = models.ForeignKey(Patient_Admission_Case , on_delete=models.CASCADE , related_name='Admission_Case_id2')
    Patient_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Pateiant_No_Case_Visit_Section2', null=True, blank=True)
    Section = models.ForeignKey(Admission_Section , on_delete=models.CASCADE , related_name='Section_Case2' ,blank=True,null=True)
    ROOM_NO = models.ForeignKey(Admission_Room , on_delete=models.CASCADE ,blank=True,null=True)
    BED = models.ForeignKey(Admission_Room_Bed, limit_choices_to={'is_activate' : True , 'in_Use':False} , on_delete=models.CASCADE,blank=True,null=True , related_name='Patient_Admission_Case_Visit_Bed_Number2')
    Start_Admission_Of_Section_Date = models.DateTimeField(blank=True,null=True )
    End_Admission_Of_Section_Date = models.DateTimeField(blank=True,null=True )
    Accept_OF_Section_Status = models.BooleanField(default=False)
    Accept_OF_Section_Date = models.DateTimeField(blank=True,null=True )
    is_Transfer = models.BooleanField(default=False)
    Visit_Status = models.BooleanField(default=False)
    Visit_Transfer = models.BooleanField(default=False)
    Visit_Transfer_id = models.CharField( max_length=200,blank=True,null=True )
    Nurse_Confirmation_Transfer = models.BooleanField(default=False)
    Asing_To_Bed_Status = models.BooleanField(default=False)
    Assgin_To_Bed_Date = models.DateTimeField(blank=True,null=True )
    is_Discharge = models.BooleanField(default=False)
    Discharge_OF_Section_Status = models.BooleanField(default=False)
    Discharge_OF_Section_Date = models.DateTimeField(blank=True,null=True )
    Discharge_Description = models.TextField(verbose_name='Transfer_Description2' ,blank=True,null=True )
    Discharge_By_User_Code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='Discharge_By_User_Code2') 
    Visit_is_Closed = models.BooleanField(default=False)
    Reason_for_Visit_closed = models.CharField( max_length=200,blank=True,null=True )
    def __str__(self):
        
        if self.Visit_is_Closed == True :
            vis = 'Visit Closed'
        else :
            vis = 'Visit Opened'
        return str(self.Patient_No) + '  - ' + str(vis)+'  - ' + str(self.Reason_for_Visit_closed)
    def get_patient_visit_list(self):
        
        get_visit = Pateint_Visit_Clinic_Case.objects.filter(Patiant_No__id=self.Admission_Case_id.patiant_no.id)
        get_visit_Admission = Patient_Admission_Case_Visit_Section.objects.filter(Admission_Case_id__patiant_no__id=self.Admission_Case_id.patiant_no.id)
        print(get_visit_Admission)
        for i in get_visit :
            visit_history = Patiant_Visit_History.objects.filter(visit_Case__id = i.id)
            print(visit_history)
        
        context = {
           
            'get_visit':get_visit ,
            'get_visit_Admission':get_visit_Admission

          }
        return context

    class Meta:
        db_table = 'Patient_Admission_Case_Visit_Section'
    





class Transfer_Tybe(models.Model):
    Tybe_Name = models.CharField( max_length=21,unique=True)
    

    def __str__(self):
        return  self.Tybe_Name
    class Meta:
        db_table = 'Transfer_Tybe'



# تحويل المريض إلى قسم آخر
class Transfer_Patient_To_ِِanother_Section(models.Model):
    Visit_Section_id = models.ForeignKey(Patient_Admission_Case_Visit_Section , on_delete=models.CASCADE , related_name='Visit_Section_id2')
    Transfer_Tybe = models.ForeignKey(Transfer_Tybe ,on_delete=models.CASCADE )
    Transfer_From_Section = models.ForeignKey(Admission_Section , on_delete=models.CASCADE , related_name='Transfer_From_Section2' ,blank=True,null=True)
    Transfer_To_Section = models.ForeignKey(Admission_Section , on_delete=models.CASCADE , related_name='Transfer_TO_Section2' ,blank=True,null=True)
    Transfer_Description = models.TextField(verbose_name='Transfer_Description' ,blank=True,null=True )
    Transfer_By_Doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True  , related_name='Transfer_By_Doctor_id2')
    Transfer_By_Doctor_Date = models.DateTimeField(auto_now_add=True ,blank=True, null=True )
    Approve_by_Nurse_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True ,  related_name='Approve_by_Nurse_id2')
    Approve_by_Nurse_Date = models.DateTimeField(auto_now_add=True ,blank=True, null=True )
    Transfer_completed_Status = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Transfer_Patient_To_ِِanother_Section'
    def __str__(self):
         return str(self.Visit_Section_id)
    


# مودل الأب لخدمات التنويم
class Patient_Admission_Case_Visit_Section_Service(models.Model):
    Admission_visit_Case = models.ForeignKey(Patient_Admission_Case_Visit_Section , on_delete=models.CASCADE ,related_name="Admission_Visit_id_%(class)s_objects")
    patiant_no = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE ,related_name="Admission_Visit_Patient_%(class)s_objects")
    ins_user_code = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    ins_user_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)  
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True




@receiver(post_save, sender=Patient_Admission_Case) 
def create_Visit_Section(sender, instance, created, **kwargs):
    if created:
        _Section = Admission_Section.objects.get(id=instance.Admission_Section.id) 
        _Patient_No = Patiant_File_NO.objects.get(id=instance.patiant_no.id)
        Patient_Admission_Case_Visit_Section.objects.create(Admission_Case_id=instance , Section = _Section , Patient_No = _Patient_No , Start_Admission_Of_Section_Date = timezone.now() , Visit_Status = True , Visit_Transfer = True)
post_save.connect(create_Visit_Section, sender=Patient_Admission_Case)



@receiver(post_save, sender=Transfer_Patient_To_ِِanother_Section) 
def create_new_visit(sender, instance, created, **kwargs):
    if created:
        id_case = Patient_Admission_Case.objects.get(id=instance.Visit_Section_id.Admission_Case_id.id)
        _Section = Admission_Section.objects.get(id=instance.Transfer_To_Section.id) 
        _Patient_No = Patiant_File_NO.objects.get(id=instance.Visit_Section_id.Patient_No.id)
        is_trans = Patient_Admission_Case_Visit_Section.objects.get(id=instance.Visit_Section_id.id)
        is_trans.Visit_is_Closed = True
        is_trans.End_Admission_Of_Section_Date = timezone.now()
        is_trans.Reason_for_Visit_closed = 'Transfer'
        is_trans.save()
        get_bed = Admission_Room_Bed.objects.filter(id=is_trans.BED.id).update(in_Use = False)
        Patient_Admission_Case_Visit_Section.objects.create(Admission_Case_id=id_case , Section = _Section , Patient_No = _Patient_No , Start_Admission_Of_Section_Date = timezone.now() , is_Transfer = True , Visit_Transfer_id = instance.Visit_Section_id.id , Visit_Status = True)
    
post_save.connect(create_new_visit, sender=Transfer_Patient_To_ِِanother_Section)




# القياسات الحيوية
class Patient_Admission_Vital_Signs(Patient_Admission_Case_Visit_Section_Service):
    Temp = models.FloatField(null=True)
    Blood_pressure = models.CharField(max_length=21,blank=True,null=True)
    spo2 = models.CharField(max_length=21,blank=True,null=True , verbose_name='Spo2 ( % )')
    Resp_rate = models.IntegerField()
    clum_1 = models.CharField(max_length=21,blank=True,null=True )
    clum_2 = models.CharField(max_length=21,blank=True,null=True )
    clum_3 = models.CharField(max_length=21,blank=True,null=True )
    class Meta:
        db_table = 'Patient_Admission_Vital_Signs'
    def __str__(self):
        return  str(self.Admission_visit_Case)  + '  - ' + str(self.patiant_no.ar_patiant_name)




# سجل تشخيص الزيارة
class Patient_Admission_Doctor_Examination_History(Patient_Admission_Case_Visit_Section_Service):
    History =models.TextField(verbose_name='History & Physical' ,blank=True, null=True)
    Diagnosis=models.TextField(verbose_name='Diagnosis',blank=True, null=True)
    Examination=models.TextField(verbose_name='Examination',blank=True, null=True)
    Doctor_Note= models.TextField(verbose_name='Doctor Note',blank=True, null=True)
    
    class Meta:
        db_table = 'Patient_Admission_Doctor_Examination_History'
    def __str__(self):
         return str(self.Admission_visit_Case)
    
 # إرسال الطلبات للتمرض   
class Patient_Admission_Order(Patient_Admission_Case_Visit_Section_Service):
    Dr_Order = models.CharField(max_length=100,blank=True,null=True)
    Nurse_Note=models.TextField(verbose_name='Nurse_Note')
    Nurse_Result_Time=models.DateTimeField(null=True, blank=True)
    order_status = models.BooleanField(default=False)
    Visit_Files = models.ImageField(upload_to=Patient_Admission_Order_Images, max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Patient_Admission_Order'
        ordering = ('-id', )
    def __str__(self):
         return str(self.Admission_visit_Case)



 
class Patient_Admission_Order_Nurse_Note(Patient_Admission_Case_Visit_Section_Service):
    Titel = models.CharField(max_length=100,blank=True,null=True , verbose_name='Titel :')
    Nurse_Note=models.TextField(verbose_name='Details :' , )
    Note_Files = models.ImageField(upload_to=Patient_Admission_Order_Images, max_length=255, null=True, blank=True , verbose_name='Upload Files :')

    class Meta:
        db_table = 'Patient_Admission_Order_Nurse_Note'
    def __str__(self):
         return str(self.Admission_visit_Case)




# طلب أشعة
class Admission_Visit_Xray(Patient_Admission_Case_Visit_Section_Service):
    Status = (
        ('Waiting Reception', 'Waiting Reception'),
        ('Waiting Report', 'Waiting Report'),
        ('Finish', 'Finish'),
    )
    Visit_History = models.ForeignKey(Patient_Admission_Doctor_Examination_History , on_delete=models.CASCADE )
    Xray_type = models.ForeignKey(Xray_type , on_delete=models.CASCADE , related_name='Xray_Type_Visits', null=True, blank=True)
    Xray_Site = models.ForeignKey(Xray_Site , on_delete=models.CASCADE , related_name='Xray_Site_Visits', null=True, blank=True)
    Status_Reception_time =models.DateTimeField(auto_now_add=True ,null=True, blank=True)  
    xray_status = models.CharField(max_length=20, choices=Status, default="Waiting Reception")
    class Meta:
        db_table = 'Patiant_admission_Xray'
    def __str__(self):
        return  str(self.id)
  