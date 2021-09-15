from django.db import models
from django.db.models import base

# => CRUD -> conexión con base de datos. Manipular bases de datos mediante clases Python

class FormatoGeneral(models.Model):
    nombre = models.CharField(max_length=200)
    numLikes = models.IntegerField(default=0)
    numVistas = models.IntegerField(default=0)

    class Meta:
        abstract = True
        #Clase abstracta => se utiliza como un formato para 
        #   estipular los métodos y atributos en una relación de herencia

    def __str__(self):
        return self.nombre
    
    def like(self):
        self.numLikes += 1
        self.save()
    
    def dislike(self):
        self.numLikes -= 1
        self.save()
    
    def nuevaVista(self):       #numVistas -> atributo de 'Genero'
                                #nuevaVista -> método
        #print(self.nombre) => Suspenso
        #print(self.numLikes) => 0
        #print(self.categoria) => models.__Categoria__
        #   Hace referencia a un objeto del tipo 'Categoria'
        self.numVistas += 1
        self.save()

class Categoria(FormatoGeneral):
    mayoriaEdad = models.BooleanField(default=False) 

class Genero(FormatoGeneral):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def nuevaVista(self):
        #Polimorfismo dinámico => se produce en relaciones de herencia
        #   Sobreescribir el contenido del método 'nuevaVista' de la clase padre
        
        #Recuperar la funcionalidad de la clase padre
        super().nuevaVista()

        #Actualizar las vistas de la categoría 
        self.categoria.nuevaVista()

class Serie(FormatoGeneral):
    generos = models.ManyToManyField(Genero)  #Especifica múltiples relaciones con objetos de tipo 'Genero'

    def like(self):
        super().like()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.like()
        
        #Like a actores
        actores = self.actor_set.all()
        for actor in actores:
            actor.like()
    
    def dislike(self):
        super().dislike()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.dislike()
        
        actores = self.actor_set.all()
        for actor in actores:
            actor.dislike()
    
    def nuevaVista(self):
        super().nuevaVista()  #Añade un nuevo like a la serie

        #Añadir numVistas a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.nuevaVista()
        
        actores = self.actor_set.all()
        for actor in actores:
            actor.nuevaVista()

class Pelicula(FormatoGeneral):    
    duracion = models.TimeField(null=True, blank=True)
    fechaLanzamiento = models.DateField(blank=True, null=True)
    generos = models.ManyToManyField(Genero)  #Especifica múltiples relaciones con objetos de tipo 'Genero'
        
    def like(self):
        super().like()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.like()
        
        #Like a actores
        actores = self.actor_set.all()
        for actor in actores:
            actor.like()
    
    def dislike(self):
        super().dislike()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.dislike()
        
        actores = self.actor_set.all()
        for actor in actores:
            actor.dislike()
    
    def nuevaVista(self):
        super().nuevaVista()  #Añade un nuevo like a la serie

        #Añadir nuevaVista a los géneros
        generos = self.generos.all()    #Obtenemos TODOS los géneros
        for genero in generos:
            genero.nuevaVista()
        
        actores = self.actor_set.all()
        for actor in actores:
            actor.nuevaVista()
  
class ContenidoPelicula(models.Model):
    idioma = models.CharField(max_length=100)
    archivo = models.FileField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.pelicula.nombre + " - " + self.idioma

class SubtitulosPelicula(models.Model):
    idioma = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    archivoSub = models.FileField()

    def __str__(self):
        return self.pelicula.nombre + " - " + self.idioma

class Temporada(FormatoGeneral):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    gratis = models.BooleanField(default=False)
    precio = models.FloatField(default=0)
    fechaLanzamiento = models.DateField()

    def numCapitulos(self):
        capitulos = self.capitulo_set.all()
        return len(capitulos)
    
    def like(self):
        super().like()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        self.serie.like()
    
    def dislike(self):
        super().dislike()  #Añade un nuevo like a la serie
        self.serie.dislike()
    
    def nuevaVista(self):
        super().nuevaVista()  #Añade un nuevo like a la serie
        self.serie.nuevaVista()


class Capitulo(FormatoGeneral):
    duracion = models.TimeField(null=True, blank=True)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)

    def like(self):
        super().like()  #Añade un nuevo like a la serie

        #Añadir likes a los géneros
        self.temporada.like()
    
    def dislike(self):
        super().dislike()  #Añade un nuevo like a la serie
        self.temporada.dislike()
    
    def nuevaVista(self):
        super().nuevaVista()  #Añade un nuevo like a la serie
        self.temporada.nuevaVista()

class ContenidoSerie(models.Model):
    idioma = models.CharField(max_length=100)
    archivo = models.FileField()
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.capitulo.nombre + " - " + self.idioma

class SubtitulosSerie(models.Model):
    idioma = models.CharField(max_length=100)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    archivoSub = models.FileField()

    def __str__(self):
        return self.capitulo.nombre + " - " + self.idioma

class Actor(FormatoGeneral):
    series = models.ManyToManyField(Serie)
    peliculas = models.ManyToManyField(Pelicula)


"""SHELL -> python manage.py shell

TuFlix

from Servicios.models import *



"""







"""
    PRUEBAS

    usuario: juand
    contraseña: 123


    proyecto musical.

    Musico - albumes - canciones

    models.Model -> clase Padre con la cual se establece la conexión CRUD  => tabla SQL

    models.CharField -> campo de texto de tipo SQL

    null=True -> permitir argumentos de tipo 'NULL'
    blank=True -> permitir argumentos 'vacíos'

    models.ForeignKey -> establecer conexión entre tablas SQL

    models.TimeField()  -> Almacenamiento de formato de tiempo

    on_delete=models.CASCADE => eliminar TODOS los albumes que le correspondan al músico que se haya eliminado
"""




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

from Servicos.models import *

#OBTENER INFORMACIÓN
musicos = Musico.objects.all()  -> obtener TODOS los registros de la tabla 'Musico' en base de datos
Juanes = Musico.objects.get(nombreArtistico="Juanes")   #get => esperamos como respuesta UN sólo objeto
Shakira = Musico.objects.get(nombreArtistico="Shakira")

albumesJuanes = Album.objects.filter(musico=Juanes)     #filter => esperamos posiblemente múltiples objetos


#CREAR UN NUEVO MÚSICO
Shakira = Musico.objects.create(nombreArtistico="Shakira", nombre="Shakira")
nuevoAlbum = Album.objects.create(musico=Juanes, nombre="Ordinario")

#CREAR ALBUM


"""