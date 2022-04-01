from django.contrib import admin
from .models import Client


# Register your models here.

# Permet d'afficher les clients dans la console admin
admin.site.register(Client)