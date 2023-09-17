# Generated by Django 4.2.4 on 2023-09-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_remove_lineapedido_estado_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparado', 'Preparado'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado'), ('devuelto', 'Devuelto')], default='pendiente', max_length=20),
        ),
    ]
