from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def carrito(request):
    return HttpResponse("Hola, estás en carrito/checkout")
