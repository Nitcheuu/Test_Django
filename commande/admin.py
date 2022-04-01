from django.contrib import admin
from .models import Commande

# Register your models here.

# Permet d'afficher les commandes sur le pannel administrateur
admin.site.register(Commande)