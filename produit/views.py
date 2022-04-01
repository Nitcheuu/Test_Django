from django.http import HttpResponse
from django.shortcuts import render
from .utils import *


# Create your views here.
def home(request):
    data = {
        "graphique" : get_plot(range(10), range(10))
    }
    return render(request, 'produit/accueil.html', {"graphique" : data["graphique"]})