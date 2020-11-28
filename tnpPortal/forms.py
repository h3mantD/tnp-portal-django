from django import forms
from .models import Logindata, Studdata

from django.core import validators

class loginDataForm(forms.ModelForm):

    #fname = forms.CharField(error_messages={'required':'enter your name'})
    mob_no = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(10)])
    #password = forms.PasswordInput

    class Meta:
        model = Logindata
        #fields = "__all__"
        exclude = ['info_stat']
        labels = {
            'fname':'First Name', 
            'lname':'Last Name',
            'e_mail': 'Email',
            'mob_no': 'Contanct Number',
            'uname': 'Username',
            'password': 'Password',
            }
        error_messages = {
            'mob_no': {'required': 'something is wrong!!!!!', },
        }
        widgets = {
            'password': forms.PasswordInput,
            #'mob_no': forms.CharField,
        }

BRANCH_CHOICES = [
    ('cs', 'Computer'),
    ('it', 'Information Technology'),
]

CLASS_CHOICES= [
    ('fe', 'FE'),
    ('se', 'SE'),
    ('te', 'TE'),
    ('be', 'BE'),
    ]



class studDataForm(forms.ModelForm):

    class Meta:
        model = Studdata
        fields = "__all__"
        labels = {
            'fname':'First Name', 
            'lname':'Last Name',
            'e_mail': 'Email',
            'mob_no': 'Contanct Number',
            'b_name': 'Branch',
            'cyear' : 'Class',
            'tenth' : '10th Marks',
            'twelth': '12th Marks',
            'nback' : 'Total Number of Backlogs',
            'add_info': 'Additional Information',
        }
        widgets = {
            'add_info' : forms.Textarea,
            'fname' : forms.TextInput(attrs={'readonly':'readonly', }),
            'lname' : forms.TextInput(attrs={'readonly':'readonly'}),
            'cyear' : forms.Select(choices=CLASS_CHOICES),
            'b_name': forms.Select(choices=BRANCH_CHOICES),
            #'studid' : forms.NumberInput(attrs={''readonly:'readonly', 'class':'form-control is-invalid'}),
            'studid' : forms.HiddenInput(attrs={'readonly':'readonly'}),

        }
        error_messages = {
            'roll':
                {'required':'Enter your roll Number'}
        }