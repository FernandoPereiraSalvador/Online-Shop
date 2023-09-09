from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=500)
    introduccion = models.CharField(max_length=50)
    imagen_principal = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    video_url = models.URLField(blank=True)
    imagenes = models.ManyToManyField('Imagen', blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    imagen = models.ImageField(upload_to='blog/imagenes/')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"
