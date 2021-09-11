from django.db import models

# Crear los modelos de nuestro Checkout

class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=100)      #CharField  -> información de texto
    dcto = models.FloatField(default=0)             #FloatField -> permite almacenar números decimales-
                                                    #default    -> define un valor por defecto (en caso de que no se defina)
    total = 0

class Producto(models.Model):
    opciones = (
        ("Mujer", "M"),
        ("Hombre", "H")
    )
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.CharField(choices=opciones, max_length=10)  #chocices => tener una estructura que contenga diferentes opciones
    cod_barras = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        #Brindar una identificación general en base de datos (sección 'Admin')
        return self.nombre

class Item (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)        #ES un objeto del tipo producto
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.producto.nombre
    
    def subtotal(self):
        #subtotal = precioProducto*cantidad
        return self.producto.precio*self.cantidad

"""SQL  -> Cuando se hacen cambios en models.py...
python manage.py makemigrations
python manage.py migrate
"""

"""SHELL

from Checkout.models import *

#Creación productos => UNA SOLA VEZ
Jeans = Producto.objects.create(nombre="Jeans", precio=100000, categoria="M", cod_barras="101")

Camisa = Producto.objects.create(nombre="Camisa", precio=50000, categoria="H", cod_barras="102")

#Desde la segunda vez en adelante... => obtener objetos de productos

Jeans = Producto.objects.get(nombre="Jeans")
Camisa = Producto.objects.get(nombre="Camisa")

-------------------------------------------------------------------------------------------------

#Creación carrito => UNA SOLA VEZ

Car1 = CarritoCompras.objects.create(usuario="1", dcto=0.0)

#Desde la segunda vez en adelante... => obtener objetos de carritoCompras

Car1 = Producto.objects.get(usuario="1")

---------------------------------------------------------------------------------------

#SOLO LA PRIMERA VEZ
item = Item.objects.create(producto=Jeans, carrito=Car1, cantidad=2)

#Desde la segunda vez en adelante... => obtener objetos de carritoCompras

item = Item.objects.get(id=1)

item.subtotal()

"""