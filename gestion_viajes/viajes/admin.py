from django.contrib import admin
from .models import Usuario, Paquete, Contrato, Deposito, Reserva

admin.site.register(Usuario)
admin.site.register(Paquete)
admin.site.register(Contrato)
admin.site.register(Deposito)
admin.site.register(Reserva)
