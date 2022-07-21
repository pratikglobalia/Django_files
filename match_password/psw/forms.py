
from django import forms

class Matchpass(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='re-password',widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valrpass = self.cleaned_data['repassword']
        if valpass != valrpass:
            raise forms.ValidationError('Password does not match')