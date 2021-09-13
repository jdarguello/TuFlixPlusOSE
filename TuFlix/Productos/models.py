from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class FamiliaProductos(models.Model):
    nombre = models.CharField(max_length=200)               #String = CharField
    presentacion = CharField(max_length=300)         #
    dcto = models.IntegerField(default=0)                 #int = IntegerField
    cantidadMinim = models.IntegerField(default=0)        #Para aplicar dcto

    def __str__(self):
        #Identifica un objeto
        return self.nombre

class Producto(models.Model):
    familia = models.ForeignKey(FamiliaProductos, on_delete=models.CASCADE)
    #on_delete => estipula la forma en cómo se elimina un producto mediante su conexión con la 'FamiliaProductos'
    presentacion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.familia.nombre + " - " + self.presentacion

class Item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.producto.__str__()
    
    def subtotal(self):
        #subtotal = cantidad*PrecioUnitario
        return self.cantidad*self.producto.precio