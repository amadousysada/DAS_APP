from django import forms
from django.forms.widgets import Input
from ser_retraite import models
from django.forms import ModelChoiceField, ModelForm
from django.db import models as md

class Html5EmailInput(Input):
    input_type = 'email'

class UploadFileForm(forms.Form):
    file = forms.FileField()





class EngagementForm(ModelForm):

    class Meta:
        model = models.Engagement
        exclude = ('employe','date_en',)
        widgets = {
            # 'date_en':forms.DateInput(attrs={'class': 'datepicker'}),
            'motif': forms.Textarea(attrs={'cols': 22, 'rows': 2}),

        }
