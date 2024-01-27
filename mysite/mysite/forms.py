from django import forms
from django.core.validators import EmailValidator

class contactform(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.CharField(validators=[EmailValidator()])
    current_website = forms.CharField(max_length=100)
    business_do = forms.CharField(widget=forms.Textarea)
