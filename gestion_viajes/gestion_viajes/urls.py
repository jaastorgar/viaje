from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),
    
    # Incluir las rutas de la aplicación 'viajes'
    path('', include('viajes.urls')),
]
