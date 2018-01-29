from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from import_export import resources
from core.models import Employe

class EmployeResource(resources.ModelResource):

    class Meta:
        model = Employe


class EmployeAdmin(ImportExportModelAdmin):
    # list_display = ['matricule', 'cnam', 'nom_prenom', 'date_emb', 'date_dep', 'statut']
    search_fields = ['matricule']
    # resource_class = EmployeResource

admin.site.register(Employe,EmployeAdmin)