
from .models import *
from django import forms
from .models import *
from Patient_Visit.models import *


class Patiant_File_NO_Form(forms.ModelForm):
    #birth_date = forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date' ,} , required=False),
    mobile_no = forms.IntegerField(required=True)
    #social_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'pattern':'([0-9]{2})(,[0-9]{2})*',}))
    def __init__(self, *args, **kwargs):
        super(Patiant_File_NO_Form, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
    class Meta:
        model = Patiant_File_NO
        fields = ['patiant_no_form' ,'social_number', 'ar_patiant_name' ,'en_patiant_name' ,'birth_date' , 'gender', 'nationalty', 'mobile_no']
        widgets = {
            'birth_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'social_number': forms.NumberInput()
            }


class Reception_Pateint_Visit_Form(forms.ModelForm):
    Patiant_No = forms.CharField()
    class Meta:
        model = Pateint_Visit
        fields = ['Patiant_No' ,'Patiant_Mode', 'Clinic_Name' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
        self.fields['Patiant_No'].widget.attrs['id'] = "Clinic_Reception_File_NO"
        self.fields['Patiant_No'].queryset = Patiant_File_NO.objects.none()
        if 'Patiant_No' in self.data:
            self.fields['Patiant_No'].queryset = Patiant_File_NO.objects.all()
        elif self.instance.pk:
            self.fields['Patiant_No'].queryset = Patiant_File_NO.objects.all().filter(pk=self.instance.Patiant_No.pk)
