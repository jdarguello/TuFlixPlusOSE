from django.contrib import admin
from django.urls import path, include

#URLBASE - Proyecto => Principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('Servicios.urls')),
    path('checkout/', include('Checkout.urls'))
]

