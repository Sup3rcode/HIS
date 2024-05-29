
from .models import *
from django import forms
from App_Home.models import *
from Patient_Visit.models import *
from Admission.models import *
from Nurse.models import *

class Patiant_Visit_Case_Form(forms.ModelForm):
    class Meta:
        model = Patiant_Visit_History
        fields = ['History', 'Diagnosis', 'Examination', 'Doctor_Note']

    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Case_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })


class Patiant_Visit_Order_Form(forms.ModelForm):
    class Meta:
        model = Patiant_Visit_Order
        fields = ['Dr_Order', ]

    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Order_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })



class Patient_Admission_Case_Form(forms.ModelForm):
    class Meta:
        model = Patient_Admission_Case
        fields = ['Admission_Section', 'Admission_Description']

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Case_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })




class Patiant_Visit_Xray_Form(forms.ModelForm):
    class Meta:
        model = Patiant_Visit_Xray
        fields = ['Xray_type', 'Xray_Site']

    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Xray_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Report_Xray_Form(forms.ModelForm):
    class Meta:
        model = Patiant_Visit_Xray_Report
        fields = ['Report_details']

    def __init__(self, *args, **kwargs):
        super(Report_Xray_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })



class Patient_Admission_Case_Form(forms.ModelForm):
    class Meta:
        model = Patient_Admission_Case
        fields = ['Admission_Section', 'Admission_Description']

    def __init__(self, *args, **kwargs):
        super(Patient_Admission_Case_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

class Visit_Close_Form(forms.ModelForm):
    Close_Details = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Pateint_Visit_Clinic_Case
        fields = ['Close_Details',]

    def __init__(self, *args, **kwargs):
        super(Visit_Close_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
class Patiant_Visit_Ruuselt_Order_Form(forms.ModelForm):
    class Meta:
        model = Patiant_Visit_Order
        fields = ['Nurse_Note', 'Visit_Files']

    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Ruuselt_Order_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

