from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db.models import Sum, F, FloatField

from tienda.models import Producto

User = get_user_model()


class Pedido(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('preparado', 'Preparado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
        ('devuelto', 'Devuelto'),
    )

    estado = models.CharField(max_length=20, choices=ESTADOS, default=ESTADOS[0][0])

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio") * F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class LineaPedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Línea Pedido'
        verbose_name_plural = 'Líneas pedidos'
        ordering = ['id']
