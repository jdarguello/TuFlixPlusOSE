from django.urls import path
from Servicios.views import vistaEjemplo

#SERVICIOS - Aplicación

#NO ES OBLIGATORIO CREARLO

urlpatterns = [
    path('ejemplo', vistaEjemplo)
]