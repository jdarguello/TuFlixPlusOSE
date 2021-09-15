from django.contrib import admin

from Servicios.models import *

# Register your models here.
admin.site.register(Actor)
admin.site.register(Categoria)
admin.site.register(Genero)
admin.site.register(Serie)
admin.site.register(Pelicula)
admin.site.register(Temporada)
admin.site.register(Capitulo)
admin.site.register(ContenidoPelicula)
admin.site.register(SubtitulosPelicula)
admin.site.register(ContenidoSerie)
admin.site.register(SubtitulosSerie)