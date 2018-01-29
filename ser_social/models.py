from django.db import models

# Create your models here.


class Pelerinage(models.Model):
    date_pel = models.DateField(auto_now=False, auto_now_add=False,blank=False)
    frais = models.IntegerField(null=True)

    def __str__(self):
        return self.date_pel