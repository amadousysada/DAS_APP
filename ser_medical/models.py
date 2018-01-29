from django.db import models
from django.contrib import admin
from core.models import Employe
from import_export.admin import ImportExportModelAdmin
# Create your models here.

SENS_CHOICES = (
            ('', '----------------'),
            ('C', 'C'),
            ('D', 'D'),
        )
TYPE_CLI_CHOICES = (
            ('', '----------------'),
            ('Local', 'Local'),
            ('Etranger', 'Etranger'),
        )
TYPE_ORD_CHOICES = (
            ('', '----------------'),
            ('0', 'Lunette'),
            ('1', 'Dent'),
        )
EMETTEUR_CHOICES = (
            ('', '----------------'),
            ('Service Action Sociale', 'Service Action Sociale'),
            ('Service Medical', 'Service Medical'),
            ('Service Retraite', 'Service Retraite'),
        )

AVIS_CHOICES = (
        ('', '----------------'),
        ('defavorable', 'defavorable'),
        ('favorable', 'favorable'),
    )


class Droits(models.Model):
    date_rec = models.DateTimeField(auto_now=False, auto_now_add=False)
    montant = models.IntegerField(null=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type = models.ForeignKey('TypeDroit', on_delete=models.CASCADE)


class Ordonnances(models.Model):
    reference = models.IntegerField(primary_key=True)
    date_soum = models.DateTimeField(auto_now=True, auto_now_add=False)
    montant = models.IntegerField(null=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    montant_rem = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_ORD_CHOICES)

    def __str__(self):
        return self.reference


class Clinique(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    libele = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CLI_CHOICES)
    # type = models.ForeignKey('TypeClinique', on_delete=models.CASCADE)
    def __str__(self):
        return self.libele


class Soins(models.Model):
    Nom_prenom = models.CharField(max_length=100)
    id_patient = models.CharField(max_length=30)
    description = models.TextField(null=True)
    Matricule = models.ForeignKey(Employe, on_delete=models.CASCADE)
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)
    date_soin = models.DateTimeField(auto_now=True, auto_now_add=False)
    chef_sec = models.CharField(max_length=100, choices=AVIS_CHOICES, null=True)
    chef_serv = models.CharField(max_length=100, choices=AVIS_CHOICES, null=True)
    dir = models.CharField(max_length=100, choices=AVIS_CHOICES, null=True)


class AyDroits(models.Model):
    nom_prenom = models.CharField(max_length=30)
    statut = models.CharField(max_length=10)
    date_de_naiss = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nom_prenom


class TypeDroit(models.Model):
    libele = models.CharField(max_length=50)

    def __str__(self):
        return self.libele


class TypeSoins(models.Model):
    libele = models.CharField(max_length=50)

    def __str__(self):
        return self.libele


class TypeClinique(models.Model):
    libele = models.CharField(max_length=50)

    def __str__(self):
        return self.libele


class PieceComptable(models.Model):
    emetteur = models.CharField(max_length=100, choices=EMETTEUR_CHOICES)
    objet = models.CharField(max_length=100)
    date_p = models.DateTimeField(auto_now=True)
    compte = models.IntegerField()
    intitule = models.TextField()
    libele = models.TextField()
    montant = models.IntegerField()
    sens = models.CharField(max_length=1, null=False, choices=SENS_CHOICES)
    beneficiaire = models.ForeignKey(Employe, on_delete=models.CASCADE)


class CliniqueAdmin(admin.ModelAdmin):
    search_fields = ['code']
admin.site.register(Clinique, CliniqueAdmin)