from django.db import models

# Crear los modelos de nuestro Checkout

"""
usuario: juand
contraseña: 123

python manage.py createsuperuser


CAMBIOS EN MODELS => python manage.py makemigrations
                     python manage.py migrate
"""



class CarritoCompras(models.Model):
    #ATRIBUTOS => define directamente los argumentos de la tabla SQL
    usuario = models.CharField(max_length=100)      #CharField  -> información de texto
    dcto = models.FloatField(default=0)             #FloatField -> permite almacenar números decimales-
                                                    #default    -> define un valor por defecto (en caso de que no se defina)
    fecha = models.DateField(auto_now_add=True, blank=True, null=True)

    #MÉTODOS
    def __str__(self):
        #permite especificar la información de los objetos en base de datos
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        #get                            => permite obtener UN objeto que cumpla una condición específica
        #filter                         => permite obtener TODOS los objetos que cumplan una condición <= MÁS AMPLIO
        #<nomClase_minuscula>_set.all() => obtiene TODOS los objetos que tengan conexión con el objeto 'CarritoCompras'
        total = 0
        #items = self.item_set.all() 
        items = Item.objects.filter(carrito=self)
        for item in items:
            total += item.subtotal()
        return total

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
    #<nomClase_minuscula>_set.all()     => ForeignKey


    #ForeignKey => establecer una conexión entre el objeto 'Item' y 'CarritoCompras'
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)        #ES un objeto del tipo producto
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    #models.ForeignKey()    => establece una relación entre tablas SQL.
    #                       => establece una relación entre objetos Python

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