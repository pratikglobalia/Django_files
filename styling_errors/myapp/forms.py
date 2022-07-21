from django import forms

class Styleerror(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter your name'})
    email = forms.EmailField(error_messages={'required':'Enter your email'},min_length=5)
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password'})
