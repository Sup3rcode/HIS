from django import forms
from .models import *


class Patient_Admission_Vital_Signs_Form(forms.ModelForm):
    class Meta:
        model = Patient_Admission_Vital_Signs
        fields = ['Temp', 'spo2',   'Resp_rate']
        
    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Vital_Signs_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })




class Patient_Admission_Nurse_Note_Form(forms.ModelForm):
    Note_Files = forms.ImageField(widget = forms.FileInput(attrs={"accept" : "image/png, image/gif, image/jpeg"}))
    #Note_Files: forms.CharField(widget=forms.I(attrs={'rows':2}))
    class Meta:
        model = Patient_Admission_Order_Nurse_Note
        fields = [ 'Titel' , 'Nurse_Note', 'Note_Files']

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Nurse_Note_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control col-md-4',
            })

class Patient_Admission_Doctor_Visit_Case_Form(forms.ModelForm):
    class Meta:
        model = Patient_Admission_Doctor_Examination_History
        fields = ['History', 'Diagnosis', 'Examination', 'Doctor_Note']

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Doctor_Visit_Case_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })




class Patient_Admission_Doctor_Visit_Order_Form(forms.ModelForm):
    class Meta:
        model = Patient_Admission_Order
        fields = ['Dr_Order', ]

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Doctor_Visit_Order_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Patiant_Admission_Ruuselt_Order_Form(forms.ModelForm):
    
    Visit_Files = forms.ImageField(label='Select a file', widget = forms.FileInput(attrs={"accept" : "image/png, image/gif, image/jpeg"}))
    class Meta:
        model = Patient_Admission_Order
        fields = ['Nurse_Note', 'Visit_Files']
    
    def __init__(self, *args, **kwargs):
        super(Patiant_Admission_Ruuselt_Order_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Patient_Admission_Doctor_Transfer_Form(forms.ModelForm):
    
    
    class Meta:
        model = Transfer_Patient_To_ِِanother_Section
        fields = [  'Visit_Section_id',  'Transfer_From_Section', 'Transfer_Tybe', 'Transfer_To_Section' , 'Transfer_Description']
        

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Doctor_Transfer_Form, self).__init__(*args, **kwargs)
        
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Patient_Admission_Doctor_Discharge_Form(forms.ModelForm):
    
    class Meta:
        model = Patient_Admission_Case_Visit_Section
        fields = ['Discharge_Description']

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Doctor_Discharge_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Patiant_admission_Xray_Form(forms.ModelForm):
    class Meta:
        model = Admission_Visit_Xray
        fields = ['Xray_type', 'Xray_Site']

    def __init__(self, *args, **kwargs):
        super(Patiant_admission_Xray_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
