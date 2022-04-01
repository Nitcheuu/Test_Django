from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def liste_commande(request):
    # Permet de faire un lien entre le fihcier HTML qui contient le template et la route
    return render(request, 'commande/liste_commande.html')
