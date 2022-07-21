from django import forms

class Formvalidation(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 4:
            raise forms.ValidationError('name should be more than or equal 4')
        if len(valemail) < 10:
            raise forms.ValidationError('email should be more than or equal 10')
