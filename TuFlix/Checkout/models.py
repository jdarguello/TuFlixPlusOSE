from django.db import models
from django.db.models import base

# Construcción de la lógica de un carrito de compras. CRUD => SQL
#Cada vez se efectúe un cambio (atributos) => python manage.py makemigrations     python manage.py migrate

#USUARIO ADMIN => usuario: juand    contraseña: 123

#Crear súper usuario => python manage.py createsuperuser

#SERVIDOR LOCAL => python manage.py runserver

class CarritoCompras(models.Model):
    #conexión con usuario...
    #Conexión con productos
    usuario = models.CharField(max_length=100)
    dcto = models.FloatField(blank=True, null=True)
    cantidadMinima = models.IntegerField(default=5)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)
    
    def Total(self):
        items = self.item_set.all()     #=> Traemos TODOS los items del carrito de compras
        total = 0
        for item in items:
            total += item.subtotal()
        return total

class Producto(models.Model):
    categorias = (
        ("Frutas", "F"),
        ("Verduras", "V")
    )

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.CharField(choices=categorias, max_length=10)        #chocices= -> atributo que permite brindar una categorización
    codigo = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        #Identifica el objeto
        return self.nombre

class Item(models.Model):
    #item = {'Sandalias':3}
    
    #ForeignKey => Establece una conexión entre tablas SQL

    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)   #Si se borra el carrito, borre todos items
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)          #Es independiente del producto => BUSCAR SOLUCIÓN
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto.nombre + " - " + self.carrito.usuario
    
    def subtotal(self):
        #subtotal = cantidad*PrecioUnitario         self.producto => Objeto de tipo 'Producto'
        return self.cantidad*self.producto.precio
    
"""SHELL => zona de depuración de pruebas de Django.
            1. Hacer pruebas CRUD
            2. Probar la lógica de un algoritmo en Django

python manage.py shell

from Checkout.models import * => Importar todas las clases

#---------OBTENER INFORMACIÓN--------------
items = Item.objects.all()  => Obtenemos todos los items registrados (objetos tipo 'Item')

#Obtener un sólo objeto
item = Item.objects.get(<nom_atributo> = valor)         => Trae un item particular
item = Item.objects.filter(<nom_atributo> = valor)      => Trae TODOS los items que cumplan la condición

#Obtención de objetos de forma 'indirecta'
carritoJuand = CarritoCompras.objects.get(usuario="juand")

items = carritoJuand.item_set.all()                 =>Trae todos los items del carrito de compras 'carritoJuand'
"""
