from django.db import models
from core.models import *

# Create your models here.


class Engagement(models.Model):
    date_en = models.DateField(auto_now=False, auto_now_add=False,blank=False)
    montant = models.IntegerField(null=True)
    motif = models.TextField(null=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type = models.ForeignKey('TypeEng', on_delete=models.CASCADE)


class TypeEng(models.Model):
    libele = models.CharField(max_length=50)

    def __str__(self):
        return self.libele


class TypeEngAdmin(admin.ModelAdmin):
    search_fields = ['libele']

class EngagementAdmin(admin.ModelAdmin):
    search_fields = ['montant']
# admin.site.register(Employe, EmployeAdmin)
admin.site.register(TypeEng, TypeEngAdmin)
admin.site.register(Engagement, EngagementAdmin)