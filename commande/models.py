from django.db import models

# Create your models here.
class Commande(models.Model):

    STATUS= (
        ("en cours", "en cours"),
        ("non livré", "non livré"),
        ("livré", "livré")
    )

    #client:
    #produit:
    status: models.CharField = models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation: models.DateField = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.date_creation)