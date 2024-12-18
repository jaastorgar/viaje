from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paquete/<int:paquete_id>/', views.detalles_paquete, name='detalles_paquete'),
    path('registrar-contrato/', views.registrar_contrato, name='registrar_contrato'),
    path('registrar-deposito/', views.registrar_deposito, name='registrar_deposito'),
    path('estado-cuenta/<int:apoderado_id>/', views.estado_cuenta, name='estado_cuenta'),
]
