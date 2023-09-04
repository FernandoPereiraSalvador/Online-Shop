from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido


@login_required(login_url="")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.username,
        emailusuario=request.usermail,
    )

    messages.success(request,"El pedido se ha creado correctamente")

    return redirect("../tienda")
