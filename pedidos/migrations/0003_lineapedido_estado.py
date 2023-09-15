# Generated by Django 4.2.4 on 2023-09-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_remove_lineapedido_pedido_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineapedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('preparado', 'Preparado'), ('enviado', 'Enviado'), ('recogido', 'Recogido'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado'), ('devuelto', 'Devuelto')], default='pendiente', max_length=20),
        ),
    ]
