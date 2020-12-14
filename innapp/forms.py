
from django import forms
from innapp import models

class AvailibiltyForm(forms.Form):
    room_categories = ( ('WB', 'bathroom'), ('NB', 'no bathroom'))
    
    room_category = forms.ChoiceField(choices=room_categories, required=True)

    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True,  input_formats=["%Y-%m-%dT%H:%M", ])