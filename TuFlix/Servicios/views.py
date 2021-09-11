from django.shortcuts import render
from django.http import HttpResponse

from Servicios.models import Musico

# => Lógica del backend
def vistaEjemplo(request):
    #request -> contiene la información del usuario
    Juanes = Musico.objects.get(nombreArtistico="Juanes")
    return HttpResponse("Estas en la aplicación de 'Servicios' " + Juanes.nombreArtistico)
