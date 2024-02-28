from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Producto, GrupoProducto



class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_lista.html'  # Nombre del template

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = '__all__'  # O puedes especificar los campos que deseas mostrar en el formulario

    def get_success_url(self):
        return reverse_lazy('producto_detalle', kwargs={'pk': self.object.pk})

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = '__all__'  # O puedes especificar los campos que deseas mostrar en el formulario

    def get_success_url(self):
        return reverse_lazy('producto_detalle', kwargs={'pk': self.object.pk})

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('lista_productos')

    

class GrupoProductoListView(ListView):
    model = GrupoProducto
    template_name = 'grupoproducto_lista.html'  # Nombre del template

class GrupoProductoDetailView(DetailView):
    model = GrupoProducto
    template_name = 'grupoproducto_detail.html'  # Nombre del template
    context_object_name = 'grupoproducto'

class GrupoProductoCreateView(CreateView):
    model = GrupoProducto
    template_name = 'grupoproducto_form.html'  # Nombre del template
    fields = ['nombre', 'descripcion']  # Campos del formulario para crear un nuevo grupo de productos
    def get_success_url(self):
        return reverse_lazy('grupo_detalle', kwargs={'pk': self.object.pk})

class GrupoProductoUpdateView(UpdateView):
    model = GrupoProducto
    template_name = 'producto_form.html'  # Nombre del template
    fields = ['nombre', 'descripcion']  # Campos del formulario para actualizar un grupo de productos existente

class GrupoProductoDeleteView(DeleteView):
    model = GrupoProducto
    template_name = 'grupoproducto_confirm_delete.html'  # Nombre del template
    success_url = reverse_lazy('lista_grupos')  # URL a la que redirigir después de eliminar un grupo de productos