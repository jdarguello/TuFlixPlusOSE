from django.contrib import admin
from Servicios.models import Album, Cancion, Musico

# Register your models here.
admin.site.register(Musico)
admin.site.register(Album)
admin.site.register(Cancion)