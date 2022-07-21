from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widget = {'name':forms.TextInput(attrs={'class':'myclass'}),
                  'passwoed':forms.PasswordInput(attrs={'class':'mypass'})}