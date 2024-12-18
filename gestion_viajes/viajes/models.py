from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_usuario


class Paquete(models.Model):
    nombre = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.destino}"


class Contrato(models.Model):
    cliente = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_viaje = models.DateField()
    numero_alumnos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.destino}"


class Deposito(models.Model):
    apoderado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Depósito de {self.apoderado.nombre_usuario} - ${self.monto}"


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.nombre_usuario} - {self.paquete.nombre}"
