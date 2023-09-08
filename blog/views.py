from django.shortcuts import render, get_object_or_404
from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request,"blog/blog.html",{"posts":post})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html",{'categoria':categoria, "posts":posts })

def detalle_articulo(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_articulo.html', {'post': post})