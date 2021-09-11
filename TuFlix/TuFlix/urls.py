from django.contrib import admin
from django.urls import path, include

#URLS oficiales del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('Servicios.urls'))
]
