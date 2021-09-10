from django.db import models

# => CRUD -> conexión con base de datos. Manipular bases de datos mediante clases Python

"""
    BEAT-E -> proyecto musical.

    Musico - albumes - canciones

    models.Model -> clase Padre con la cual se establece la conexión CRUD  => tabla SQL

    models.CharField -> campo de texto de tipo SQL

    null=True -> permitir argumentos de tipo 'NULL'
    blank=True -> permitir argumentos 'vacíos'

    models.ForeignKey -> establecer conexión entre tablas SQL

    models.TimeField()  -> Almacenamiento de formato de tiempo

    on_delete=models.CASCADE => eliminar TODOS los albumes que le correspondan al músico que se haya eliminado
"""

class Musico(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    nombreArtistico = models.CharField(max_length=100)

    def __str__(self):
        #Especificamos qué se va a mostrar
        return self.nombreArtistico

class Album(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    caratula = models.ImageField(null=True, blank=True)
    fechaCreacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Canciones(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField(null=True, blank=True)
    archivoAudio = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nombre


"""SQL

CREATE TABLE Servicios_Musico(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL
);

"""

"""SHELL    -> herramienta que permite ejecutar código Python del proyecto Django
                python manage.py shell

                Podemos hacer lo siguiente:     SISTEMA DE DEPURACIÓN DE CÓDIGO
                    1. Probar código CRUD
                    2. Verificar la lógica de un algoritmo

"""