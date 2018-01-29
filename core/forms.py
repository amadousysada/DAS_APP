from django import forms
from django.forms.widgets import Input
from django.forms import ModelChoiceField, ModelForm
from django.db import models as md

class Html5EmailInput(Input):
    input_type = 'email'

class UploadFileForm(forms.Form):
    file = forms.FileField()


class LoginForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']
        length = len(password)
        if length < 8:
            raise forms.ValidationError("le mot de passe doit etre au moins de 8 caractere")
        return password