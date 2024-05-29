
from .models import *
from django import forms
from .models import *
from Visit_Clinic.models import *

class Vital_Signs_Form(forms.ModelForm):
    class Meta:
        model = Visit_Vital_Signs
        fields = ['Temp', 'spo2', 'Body_weight', 'Height',  'Resp_rate']

    def __init__(self, *args, **kwargs):
        super(Vital_Signs_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
            
import imghdr
class Patiant_Visit_Ruuselt_Order_Form(forms.ModelForm):
    
    Visit_Files = forms.ImageField(label='Select a file', widget = forms.FileInput(attrs={"accept" : "image/png, image/gif, image/jpeg"}))
    class Meta:
        model = Patiant_Visit_Order
        fields = ['Nurse_Note', 'Visit_Files']
    def validate_docfile(self):
        file = self.cleaned_data.get("Visit_Files")
        if file:
            if imghdr.what(file.read()) != "jpeg":
                raise forms.ValidationError("Please upload a .gif file")
            file.seek(0)
        return file
    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Ruuselt_Order_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })


class Patiant_Visit_Nurse_Note_Form(forms.ModelForm):
    Note_Files = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    class Meta:
        model = Patiant_Visit_Nurse_Note
        fields = ['Nurse_Note', 'Note_Files']

    def __init__(self, *args, **kwargs):
        super(Patiant_Visit_Nurse_Note_Form, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

#<label>Your Image File
  #<input type="file" name="myImage" accept="image/png, image/gif, image/jpeg" />
#</label>