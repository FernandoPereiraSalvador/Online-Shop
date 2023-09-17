from django.urls import path
from ProyectoWebApp import views
from . import views
from .views import panel_usuario

urlpatterns = [
    path('panel usuario',panel_usuario, name="panel_usuario"),
    path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('anular_pedido/<int:pedido_id>/', views.anular_pedido, name='anular_pedido'),
]
