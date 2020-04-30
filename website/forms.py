from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class CheckoutForm(forms.Form):
    appartment_address = forms.CharField() 
    street_address = forms.CharField()
    country = CountryField()
    country = CountryField(blank_label='(select country)')
    zip = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect() )