from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Comentario
from pedidos.models import Pedido, LineaPedido


# Función auxiliar para renderizar la página común

@login_required
def panel_usuario(request):
    # Obtener información del usuario autenticado
    usuario = request.user

    # Consultar los comentarios del usuario
    comentarios = Comentario.objects.filter(autor=usuario)

    # Consultar los pedidos del usuario
    pedidos = Pedido.objects.filter(user=usuario)
    linea_pedidos = LineaPedido.objects.filter(user=usuario)
    total_pedidos = []
    for pedido in pedidos:
        total_pedido = 0  # Inicializa el total para cada pedido
        for linea_pedido in pedido.lineapedido_set.all():
            if linea_pedido.producto.precio is not None and linea_pedido.cantidad is not None:
                total_pedido += linea_pedido.producto.precio * linea_pedido.cantidad
        total_pedidos.append(total_pedido)  # Agrega el total del pedido a la lista

    pedidos_info = zip(pedidos, total_pedidos, linea_pedidos)

    return render(request, 'panel usuario/panel_usuario.html',
                  {'usuario': usuario, 'comentarios': comentarios, 'pedidos_info': pedidos_info})


def eliminar_comentario(request, comentario_id):

    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        comentario.delete()
    return panel_usuario(request)


def anular_pedido(request, pedido_id):

    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
    return panel_usuario(request)
