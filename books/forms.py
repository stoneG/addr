from django import forms

class AddressForm(forms.Form):
    name = forms.CharField(max_length=100)
    line_one = forms.CharField(max_length=100)
    line_two = forms.CharField(max_length=50)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    zip_code = forms.CharField(max_length=5)
