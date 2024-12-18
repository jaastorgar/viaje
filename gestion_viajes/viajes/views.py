from django.shortcuts import render, redirect, get_object_or_404
from .models import Paquete, Contrato, Usuario, Deposito, Paquete, Reserva

# Página principal: muestra los paquetes turísticos
def home(request):
    paquetes = Paquete.objects.all()
    return render(request, 'viajes/home.html', {'paquetes': paquetes})

# Detalles de un paquete turístico
def detalles_paquete(request, paquete_id):
    paquete = get_object_or_404(Paquete, id=paquete_id)
    return render(request, 'viajes/detalles_paquete.html', {'paquete': paquete})

# Registrar contrato
def registrar_contrato(request):
    if request.method == 'POST':
        cliente = request.POST['cliente']
        destino = request.POST['destino']
        fecha_viaje = request.POST['fecha_viaje']
        numero_alumnos = request.POST['numero_alumnos']
        Contrato.objects.create(
            cliente=cliente,
            destino=destino,
            fecha_viaje=fecha_viaje,
            numero_alumnos=numero_alumnos
        )
        return redirect('home')
    return render(request, 'viajes/registrar_contrato.html')

# Registrar depósito
def registrar_deposito(request):
    if request.method == 'POST':
        apoderado_id = request.POST['apoderado']
        contrato_id = request.POST['contrato']
        monto = request.POST['monto']
        Deposito.objects.create(
            apoderado_id=apoderado_id,
            contrato_id=contrato_id,
            monto=monto
        )
        return redirect('home')
    apoderados = Usuario.objects.all()
    contratos = Contrato.objects.all()
    return render(request, 'viajes/registrar_deposito.html', {'apoderados': apoderados, 'contratos': contratos})

# Estado de cuenta
def estado_cuenta(request, apoderado_id):
    apoderado = get_object_or_404(Usuario, id=apoderado_id)
    depositos = Deposito.objects.filter(apoderado=apoderado)
    total_aportes = sum(deposito.monto for deposito in depositos)
    return render(request, 'viajes/estado_cuenta.html', {
        'apoderado': apoderado,
        'depositos': depositos,
        'total_aportes': total_aportes,
    })



# Página principal: muestra todos los paquetes turísticos
def home(request):
    paquetes = Paquete.objects.all()
    return render(request, 'viajes/home.html', {'paquetes': paquetes})

# Detalles de un paquete específico
def detalles_paquete(request, paquete_id):
    paquete = get_object_or_404(Paquete, id=paquete_id)
    return render(request, 'viajes/detalles_paquete.html', {'paquete': paquete})

def lista_paquetes(request):
    paquetes = Paquete.objects.all()
    return render(request, 'viajes/lista_paquetes.html', {'paquetes': paquetes})

# Reservar un paquete
def reservar_paquete(request, paquete_id):
    paquete = get_object_or_404(Paquete, id=paquete_id)
    usuario = Usuario.objects.first()  # Simula un usuario logueado (modifica esto según tu lógica de autenticación)
    
    if request.method == 'POST':
        Reserva.objects.create(usuario=usuario, paquete=paquete)
        return redirect('mis_reservas')

    return render(request, 'viajes/reservar_paquete.html', {'paquete': paquete})

# Mostrar las reservas del usuario
def mis_reservas(request):
    usuario = Usuario.objects.first()  # Simula un usuario logueado
    reservas = Reserva.objects.filter(usuario=usuario)
    return render(request, 'viajes/mis_reservas.html', {'reservas': reservas})

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('mis_reservas')