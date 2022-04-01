from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def liste_clients(request):
    return render(request, 'client/liste_client.html')