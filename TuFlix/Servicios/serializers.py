#Sección en donde creamos los serializadores de nuestra aplicación 'Servicios'

#Serializador => herramienta que convierte una clase Python en un archivo JSON
#               y viceversa (convierte JSON en clase Python)

from rest_framework import serializers

from Servicios.models import *

class CategoriaSerial(serializers.Serializer):         #Serializador general
    nombre = serializers.CharField(max_length=200)
    numLikes = serializers.IntegerField()
    numVistas = serializers.IntegerField()
    mayoriaEdad = serializers.BooleanField()

class CategoriaSerial2(serializers.ModelSerializer):    #Está enfocado en serializar objetos CRUD
    class Meta:
        model = Categoria   #Modelo CRUD de referencia 
        #fields = '__all__'  #Toma TODOS los atributos
        fields = ['nombre', 'numVistas', 'mayoriaEdad']

class GeneroSerial(serializers.ModelSerializer):         #Serializador general
    class Meta:
        model = Genero   #Modelo CRUD de referencia 
        fields = '__all__'  #Toma TODOS los atributos
        #fields = ['id', 'nombre', 'numVistas', 'mayoriaEdad']

class SerieSerial(serializers.ModelSerializer):         #Serializador general
    class Meta:
        model = Serie   #Modelo CRUD de referencia 
        #fields = '__all__'  #Toma TODOS los atributos
        fields = ['nombre', 'numTemporadas']

"""SHELL
    python manage.py shell

from Servicios.serializers import *

categorias = Categoria.objects.all()

accion = Genero.objects.get(nombre="Acción")

accionS = GeneroSerial(accion)

GoT = Serie.objects.get(nombre="Game of Thrones")

GS = SerieSerial(GoT)

"""