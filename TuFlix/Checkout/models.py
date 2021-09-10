from django.db import models
from django.db.models import base

# Construcción de la lógica de un carrito de compras. CRUD => SQL

class CarritoCompras(models.Model):
    #conexión con usuario...
    #Conexión con productos
    usuario = models.CharField(max_length=100)
    dcto = models.FloatField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    #def total(self):

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
        return self.nombre

class Item(models.Model):
    #item = {'Sandalias':3}
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)   #Si se borra el carrito, borre todos items
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)          #Es independiente del producto => BUSCAR SOLUCIÓN
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto.nombre + " - " + self.carrito.usuario
    


