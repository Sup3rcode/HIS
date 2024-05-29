from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
    class Meta:
        model=User
        fields = {'username', 'email','password1','password2'}


class ProfileForm(forms.ModelForm):



    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control',})
    class Meta:
        model = Profile
        fields = ['ID_number' ,'job_number' , 'gender','Employee_Type' ,'jobcatogery' ,'Nationlity' ,'DEPARTEMNTS' ,]