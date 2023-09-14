from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from blog.models import Comentario


class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Home')


def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})


@login_required
def panel_usuario(request):
    # Obtener información del usuario autenticado
    usuario = request.user

    # Consultar los comentarios del usuario
    comentarios = Comentario.objects.filter(autor=usuario)
    return render(request, 'panel usuario/panel_usuario.html', {'usuario': usuario, 'comentarios': comentarios})


def eliminar_comentario(request, comentario_id):
    usuario = request.user
    comentarios = Comentario.objects.filter(autor=usuario)

    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        comentario.delete()
    return render(request,'panel usuario/panel_usuario.html', {'usuario': usuario, 'comentarios': comentarios})

