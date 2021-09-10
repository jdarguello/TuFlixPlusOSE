from django.db import models

# Conexión CRUD

class Musico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    salario = models.IntegerField()

    def __str__(self):
        #Facilita la interpretación del contenido, para este caso, a través del nombre del artista
        return self.nombre

class Album(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_pub = models.DateField()
    caratula = models.ImageField(null=True, blank=True) #(opcional)

    #null=True, blank=True -> se emplean para que permita hacer registros
    #                         sin ese item

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField(null=True, blank=True)   #(opcional)

    def __str__(self):
        return self.nombre

"""SHELL -> depurar código del proyecto django para hacer análisis de lógica y para hacer pruebas CRUD
            python manage.py shell

from Servicios.models import *

#ACCEDER A CONTENIDO
musicos = Musico.objects.all()                      #-> obtener todos los registros en base de datos
Shakira = Musico.objects.get(nombre="Shakira")      #-> obtener un registro particular

.get()      => se emplea para importar UN sólo registro de base de datos
.filter()   => se utiliza para importar TODOS los registros que cumplan una condición

#CREAR NUEVO MÚSICO
Musico.objects.create(nombre="Shakira", salario=500000000, edad=40)

#CREAR ALBÚM
from datetime import datetime
hoy = datetime.date.today()     #<- FECHA

Album.objects.create(musico=Juanes, nombre="Normal", genero="Balada", fecha_pub=hoy)

albumesJuanes = Album.objects.filter(musico=Juanes) #se obtienen TODOS los albúmes de un artista

#CREAR

"""