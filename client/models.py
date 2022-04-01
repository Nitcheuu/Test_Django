from django.db import models


# Create your models here.
class Client(models.Model):
    nom: str
    telephone: str
    date_creation: models.DateField()

    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True) # auto_now_add génère automatiquement la date

    def __str__(self):
        return self.nom


