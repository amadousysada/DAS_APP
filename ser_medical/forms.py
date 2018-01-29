from django import forms
from django.forms.widgets import Input
from ser_medical import models
from django.forms import ModelChoiceField, ModelForm
from django.db import models as md

MOIS_CHOICES = (
    ('1', 'Janvier'),
    ('2', 'Fevrier'),
    ('3', 'Mars'),
    ('4', 'Avril'),
    ('5', 'Mai'),
    ('6', 'Juin'),
    ('7', 'Juillet'),
    ('8', 'Aout'),
    ('9', 'Septembre'),
    ('10', 'Octobre'),
    ('11', 'Novembre'),
    ('12', 'Decembre'),
)

ASSURE_CHOICES = (
        ('', '----------------'),
        ('0', 'Principale'),
        ('1', 'Famille'),
    )


class Html5EmailInput(Input):
    input_type = 'email'

class UploadFileForm(forms.Form):
    file = forms.FileField()




class SoinForm(ModelForm):

    matricule=forms.IntegerField()
    class Meta:
        model = models.Soins
        exclude = ('Matricule','chef_sec','chef_serv','dir')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(SoinForm, self).__init__(*args, **kwargs)
        self.fields['clinique'] = ModelChoiceField(queryset=models.Clinique.objects.all(),empty_label = "selectionner clini")

class CliniqueForm(ModelForm):
    class Meta:
        model = models.Clinique
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CliniqueForm, self).__init__(*args, **kwargs)
        # self.fields['type'] = ModelChoiceField(queryset=models.TypeClinique.objects.all(),empty_label = "selectionner type")


class PieceComForm(ModelForm):
    class Meta:

        model = models.PieceComptable
        exclude = ('beneficiaire',)
        widgets = {
            'intitule': forms.Textarea(attrs={'cols': 22, 'rows': 2}),
            'libele': forms.Textarea(attrs={'cols': 22, 'rows': 2}),
        }


class OrdonnanceForm(ModelForm):


    assure=forms.ChoiceField(choices=ASSURE_CHOICES)
    class Meta:
        model = models.Ordonnances
        # fields = '__all__'
        exclude = ('montant_rem','employe',)

    def __init__(self, *args, **kwargs):
        super(OrdonnanceForm, self).__init__(*args, **kwargs)
        # self.fields['type'] = ModelChoiceField(queryset=models.TypeClinique.objects.all(),empty_label = "selectionner type")



class StatsForm(forms.Form):
    mois = forms.ChoiceField(choices=MOIS_CHOICES,disabled=True)
    annee = forms.IntegerField(disabled=True)