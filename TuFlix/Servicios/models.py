from django.db import models

# Conexión CRUD

class Musico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    salario = models.IntegerField()

class Album(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_pub = models.DateField()
    caratula = models.ImageField(null=True, blank=True) #(opcional)

    #null=True, blank=True -> se emplean para que permita hacer registros
    #                         sin ese item

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField(null=True, blank=True)   #(opcional)
