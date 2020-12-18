
from django import forms
from innapp import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AvailibiltyForm(forms.Form):
    room_categories = ( ('WB', 'bathroom'), ('NB', 'no bathroom'))
    
    room_category = forms.ChoiceField(choices=room_categories, required=True)

    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True,  input_formats=["%Y-%m-%dT%H:%M", ])

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    e_mail = forms.CharField(max_length=100)
    telephone = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name' ,'e_mail', 'telephone', 'password1','password2']

