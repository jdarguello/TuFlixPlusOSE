from django.shortcuts import render
from django.http import HttpResponse


# => Lógica del backend
def vistaEjemplo(request):
    #request -> contiene la información del usuario
    return HttpResponse("Estas en la aplicación de 'Servicios'")
