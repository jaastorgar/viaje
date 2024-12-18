from django.shortcuts import render, redirect, get_object_or_404
from .models import Paquete, Reserva, Contrato, Usuario, Deposito
from .forms import ContratoForm
from django.core.mail import send_mail

# Página principal que lista los paquetes
def home(request):
    paquetes = Paquete.objects.all()
    return render(request, 'viajes/home.html', {'paquetes': paquetes})

# Detalles de un paquete específico
def detalles_paquete(request, paquete_id):
    paquete = get_object_or_404(Paquete, id=paquete_id)
    return render(request, 'viajes/detalles_paquete.html', {'paquete': paquete})

# Registrar un contrato
def registrar_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContratoForm()
    return render(request, 'viajes/registrar_contrato.html', {'form': form})

# Registrar un depósito
def registrar_deposito(request):
    if request.method == 'POST':
        apoderado_id = request.POST['apoderado']
        contrato_id = request.POST['contrato']
        monto = request.POST['monto']
        deposito = Deposito.objects.create(
            apoderado_id=apoderado_id,
            contrato_id=contrato_id,
            monto=monto
        )
        # Enviar correo electrónico al apoderado
        apoderado = Usuario.objects.get(id=apoderado_id)
        send_mail(
            'Confirmación de Depósito',
            f"Se ha registrado un depósito de ${monto} para el contrato de {deposito.contrato.cliente}.",
            'tu_correo@gmail.com',
            [apoderado.email],
            fail_silently=False
        )
        return redirect('home')
    return render(request, 'viajes/registrar_deposito.html', {
        'apoderados': Usuario.objects.all(),
        'contratos': Contrato.objects.all(),
    })

# Ver el estado de cuenta de un apoderado
def estado_cuenta(request, apoderado_id):
    apoderado = get_object_or_404(Usuario, id=apoderado_id)
    depositos = Deposito.objects.filter(apoderado=apoderado)
    total_aportes = sum(deposito.monto for deposito in depositos)
    return render(request, 'viajes/estado_cuenta.html', {
        'apoderado': apoderado,
        'depositos': depositos,
        'total_aportes': total_aportes,
    })
