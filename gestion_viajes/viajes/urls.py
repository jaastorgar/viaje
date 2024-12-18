from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # Paquetes
    path('paquete/<int:paquete_id>/', views.detalles_paquete, name='detalles_paquete'),
    path('paquetes/', views.lista_paquetes, name='lista_paquetes'),

    # Contratos y Depósitos
    path('registrar-contrato/', views.registrar_contrato, name='registrar_contrato'),
    path('registrar-deposito/', views.registrar_deposito, name='registrar_deposito'),

    # Estado de Cuenta
    path('estado-cuenta/<int:apoderado_id>/', views.estado_cuenta, name='estado_cuenta'),

    # Reservas
    path('reservar/<int:paquete_id>/', views.reservar_paquete, name='reservar_paquete'),

    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('eliminar-reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
]
