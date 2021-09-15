#Sección en donde creamos los serializadores de nuestra aplicación 'Servicios'

#Serializador => herramienta que convierte una clase Python en un archivo JSON
#               y viceversa (convierte JSON en clase Python)

from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers

class CategoriaSerial(Serializer):
    serializers.CharField()
    nombre = serializers.CharField(max_length=200)
    mayoriaEdad = serializers.BooleanField()