from django.urls import *
from . import views

urlpatterns = [
    path('',  views.liste_clients),
]
