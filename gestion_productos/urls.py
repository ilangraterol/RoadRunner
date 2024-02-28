#  gestion_productos/urls.py

from django.urls import path
from .views import ProductoListView, GrupoProductoCreateView, GrupoProductoDetailView, GrupoProductoUpdateView, GrupoProductoListView, GrupoProductoDeleteView, ProductoCreateView, ProductoDetailView, ProductoDeleteView, ProductoUpdateView

urlpatterns = [
    path('', ProductoListView.as_view(), name='lista_productos'),
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),
    path('<int:pk>/actualizar/', ProductoUpdateView.as_view(), name='producto_actualizar'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_eliminar'),

    path('grupos/', GrupoProductoListView.as_view(), name='lista_grupos'),
    path('grupos/crear/', GrupoProductoCreateView.as_view(), name='grupo_crear'),
    path('grupos/<int:pk>/', GrupoProductoDetailView.as_view(), name='grupo_detalle'),
    path('grupos/<int:pk>/actualizar/', GrupoProductoUpdateView.as_view(), name='grupo_actualizar'),
    path('grupos/<int:pk>/eliminar/', GrupoProductoDeleteView.as_view(), name='grupo_eliminar'),
]
