from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog,name="Blog"),
    path('categoria/<int:categoria_id>/',views.categoria,name="categoria"),
    path('blog/<int:post_id>/', views.detalle_articulo, name='detalle_articulo'),
]