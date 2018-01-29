from django.db import models
from ser_social.models import *
from django.contrib import admin

# Create your models here.


class Employe(models.Model):
    matricule = models.IntegerField(primary_key=True)
    cnam = models.IntegerField()
    nom_prenom = models.CharField(max_length=100)
    date_emb = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_dep = models.DateTimeField(auto_now=False, auto_now_add=False)
    statut = models.CharField(max_length=10)
    civilite = models.CharField(max_length=5, default="Homme")

    def __str__(self):
        return self.nom_prenom


class InfoEmploye(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    pelerin = models.ForeignKey(Pelerinage, on_delete=models.CASCADE)
    somme = models.IntegerField()


class Gains(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    montant = models.IntegerField(null=True)
    libele_g = models.TextField(null=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)