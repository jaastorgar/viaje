# viajes/admin.py
from django.contrib import admin
from .models import Usuario, Paquete, Reserva

admin.site.register(Usuario)
admin.site.register(Paquete)
admin.site.register(Reserva)
