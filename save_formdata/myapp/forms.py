from django import forms

class Userregistration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter name'})
    email = forms.EmailField(error_messages={'required':'Enter email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter password'})