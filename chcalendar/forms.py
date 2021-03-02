from django import forms

class CHForm(forms.Form):
    url = forms.URLField(max_length=100)