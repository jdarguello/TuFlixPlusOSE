#URLS -> CHECKOUT

from django.urls import path

from Checkout.views import carrito

urlpatterns = [
    path('carrito-compras', carrito)
]
