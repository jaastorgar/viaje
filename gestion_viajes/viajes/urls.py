# gestion_viajes/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('viajes.urls')),
]

# viajes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paquete/<int:paquete_id>/', views.detalles_paquete, name='detalles_paquete'),
]
