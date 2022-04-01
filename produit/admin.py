from django.contrib import admin
from .models import Produit


# Register your models here.
# Permet d'afficher les produits sur le pannel admin
admin.site.register(Produit)