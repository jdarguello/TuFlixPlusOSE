from django.shortcuts import render
from django.http import HttpResponse

from Servicios.models import Musico

# => Lógica del backend
def vistaEjemplo(request):
    #request -> contiene la información del usuario
    Shakira = Musico.objects.get(nombreArtistico="Shakira")
    return HttpResponse("Estas en la aplicación de 'Servicios' " + Shakira.nombreArtistico)
