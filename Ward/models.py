from django.db import models
from Patient_Visit import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from App_Home.models import *
from django.conf import settings
from datetime import datetime, timedelta
last24H = datetime.now() - timedelta(hours=24)
from django.db import models
from django.utils import timezone
import os
from django.db.models import signals
from uuid import uuid4
STATUS_CHOICES = (
        ('In Use', 'In Use'),
        ('Close', 'Close'),
        
    )

DESCRIPTION = (
        ('Semi Private', 'Semi Private'),
        ('Isolation', 'Isolation'),
        ('Nursery', 'Nursery'),
        
    )

vacant = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        
    )

MIXED_SEX = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        
    )
ROOM_SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Both', 'Both'),
        
    )

from Patient_Visit.models import *




class Admission_Section(models.Model):
    Section_Name = models.CharField( max_length=21,unique=True)
    User_Access = models.ManyToManyField(User,  blank=True) 

    def __str__(self):
        return  self.Section_Name
    class Meta:
        db_table = 'Admission_Section'



class Admission_Room(models.Model):
    Section_Name = models.ForeignKey(Admission_Section , on_delete=models.CASCADE , )
    Room_Number = models.CharField( max_length=21 )
    STATUS = models.CharField(max_length=100, choices=STATUS_CHOICES, default='In Use')
    ROOM_SEX = models.CharField(max_length=100, choices=ROOM_SEX, default='In Use')
    MIXED_SEX = models.CharField(max_length=100, choices=MIXED_SEX, default='No')
    Vacant = models.CharField(max_length=100, choices=vacant, default='No') 
    DESCRIPTION = models.CharField(max_length=100, choices=DESCRIPTION, default='Semi Private')

    def __str__(self):
        return  str(self.Section_Name) + '--' + str(self.Room_Number)

    class Meta:
        unique_together = (('Section_Name', 'Room_Number'),)
        db_table = 'Admission_Room'

class Admission_Room_Bed(models.Model):
    Room_Num = models.ForeignKey(Admission_Room , on_delete=models.CASCADE )
    Bed_Num = models.CharField( max_length=1 )
    is_activate = models.BooleanField(default=False)
    in_Use = models.BooleanField(default=False)
    Patient_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Pateiant_No_Admission_Bed', null=True, blank=True)
    class Meta:
        unique_together = (('Room_Num', 'Bed_Num'),)
        db_table = 'Admission_Room_Bed'
        
    def __str__(self):
        return  str(self.Room_Num) + '--' + str(self.Bed_Num)
