from django import forms

class postform(forms.Form):
    docfile = forms.FileField(label='Select a file',)