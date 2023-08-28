from django.shortcuts import render
from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("tienda")


def eliminar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("tienda")

def limpiar_producto(request, producto_id):
    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.limpiar_carro()

    return redirect("tienda")