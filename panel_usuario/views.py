from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Comentario


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
