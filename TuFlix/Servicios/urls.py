#URLS => SERVICIOS

from django.urls import path

#Para importar la vista de ejemplo...
from Servicios.views import vistaEjemplo

urlpatterns = [
    path("ejemplo", vistaEjemplo)
]

#localhost:8000/servicios/ -> ubicación local de 'Servicios'