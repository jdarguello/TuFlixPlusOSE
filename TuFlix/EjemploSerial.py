#Archivo de prueba

class Comentario:
    def __init__(self, email, contenido, fecha=None):
        self.email = email
        self.contenido = contenido
        self.fecha = fecha

from rest_framework import serializers

class ComentarioSerial(serializers.Serializer): #models.Model
    email = serializers.EmailField()    #models => serializers
    contenido = serializers.CharField(max_length=2000)
    fecha = serializers.DateField()

#-----------------------------------PRUEBAS-----------------------------

#Objeto == instancia de clase

com1 = Comentario("jaja@", "kakaka")

serialEjemplo = ComentarioSerial(com1)

print(serialEjemplo.data)