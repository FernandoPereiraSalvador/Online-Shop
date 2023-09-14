from django.urls import path
from ProyectoWebApp import views
from . import views
from .views import VRegistro, cerrar_sesion, logear,panel_usuario

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    path('panel usuario',panel_usuario, name="panel_usuario"),
    path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
]
