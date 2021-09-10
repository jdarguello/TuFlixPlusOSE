from django.shortcuts import render

#Para imprimir mensajes sencillos de respuesta:
from django.http import HttpResponse   

from Servicios.models import *

# Create your views here.

def vistaEjemplo(request):
    """
    request -> contiene toda la información del
               usuario que hace la petición de
               acceso a la aplicación a través de
               métodos GET y POST, principalmente.
    
    GET     -> método con el cual el usuario
               solicita acceder a una URL.
    
    POST    -> método con el cual el usuario 
               envía información a una URL.
    """
    Juanes = Musico.objects.get(nombre="Juan Esteban")

    return HttpResponse("Hola, estás en la aplicación 'Servicios', con el músico: " + Juanes.apellido)
