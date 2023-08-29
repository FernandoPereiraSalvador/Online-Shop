from django.urls import path
from ProyectoWebApp import views
from . import views
from .views import VRegistro
urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
]