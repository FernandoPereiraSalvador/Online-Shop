from django.contrib import admin
from .models import Categoria, Post, Imagen


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ImagenInline(admin.TabularInline):
    model = Post.imagenes.through


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Imagen)