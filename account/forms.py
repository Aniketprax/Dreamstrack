from django import forms
from account.models import Users


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'city', 'state', 'email', 'password', 'phno', 'college', 'school','sex','age')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email','password')