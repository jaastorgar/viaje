# viajes/models.py

from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario

class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.paquete}"


# viajes/models.py

class Contrato(models.Model):
    cliente = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_viaje = models.DateField()
    numero_alumnos = models.PositiveIntegerField()
    servicios_contratados = models.TextField()
    actividades = models.TextField()

    def __str__(self):
        return f"Contrato: {self.cliente} - {self.destino}"
