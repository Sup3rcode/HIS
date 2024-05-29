from Patient_Files.forms import *
from Visit_Clinic.forms import *
from Admission.forms import *
from Nurse.forms import *

def Visit_forms(request):
  usr = request.user.id
  context = {
      'user_id':usr ,
        'Patiant_File_NO_Form':Patiant_File_NO_Form ,
        'Reception_Pateint_Visit_Form':Reception_Pateint_Visit_Form ,


        ###   Admission Forms 
        'Patient_Admission_Vital_Signs_Form':Patient_Admission_Vital_Signs_Form ,
        'Patient_Admission_Nurse_Note_Form': Patient_Admission_Nurse_Note_Form ,
        'Patient_Admission_Doctor_Visit_Case_Form': Patient_Admission_Doctor_Visit_Case_Form ,
        'Patient_Admission_Doctor_Visit_Order_Form': Patient_Admission_Doctor_Visit_Order_Form ,
        'Patient_Admission_Doctor_Discharge_Form': Patient_Admission_Doctor_Discharge_Form ,
        'Patient_Admission_Doctor_Transfer_Form': Patient_Admission_Doctor_Transfer_Form ,
        
        
        #------------ Visit Clinic Forms ------------------
        'Xray_Form':Patiant_Visit_Xray_Form ,
        'Visit_Close_Form':Visit_Close_Form ,
        'Nurse_Order_Form':Patiant_Visit_Ruuselt_Order_Form ,
        'Visit_Case_Form' : Patiant_Visit_Case_Form ,
        'Visit_Order_Form' : Patiant_Visit_Order_Form ,
        'Visit_Admission_Form' : Patient_Admission_Case_Form ,
        'Admission_Case_Form':Patient_Admission_Case_Form ,
        'Patiant_Admission_Ruuselt_Order_Form':Patiant_Admission_Ruuselt_Order_Form

          }
  return context