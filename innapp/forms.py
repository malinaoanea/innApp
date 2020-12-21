
from django import forms
from innapp import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AvailibiltyForm(forms.Form):
    room_categories = ( ('WB', 'bathroom'), ('NB', 'no bathroom'))
    
    room_category = forms.ChoiceField(choices=room_categories, required=True)

    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", ])
    check_out = forms.DateTimeField(required=True,  input_formats=["%Y-%m-%d", ])
    number_of_rooms = forms.IntegerField(required=True)

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    class Meta:
        model = models.ClientProfile
        exclude = ['user']

