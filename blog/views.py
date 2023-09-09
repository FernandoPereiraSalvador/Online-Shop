from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import ComentarioForm
from blog.models import Post, Categoria, Comentario
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,"blog/blog.html",{"posts":post})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html",{'categoria':categoria, "posts":posts })


from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comentario
from .forms import ComentarioForm


def detalle_articulo(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(publicacion=post)

    if request.method == 'POST':
        if request.user.is_authenticated:
            formulario = ComentarioForm(request.POST)
            if formulario.is_valid():
                nuevo_comentario = formulario.save(commit=False)
                nuevo_comentario.autor = request.user
                nuevo_comentario.publicacion = post
                nuevo_comentario.save()
                return redirect('detalle_articulo', post_id=post_id)
        else:
            messages.error(request, 'Necesitas iniciar sesión para dejar un comentario.')
    else:
        formulario = ComentarioForm()

    return render(request, 'blog/detalle_articulo.html',
                  {'post': post, 'comentarios': comentarios, 'formulario': formulario})
