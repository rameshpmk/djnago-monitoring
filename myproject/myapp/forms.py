from django import forms
from .models import IPAddress


class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ['address','monitor']
