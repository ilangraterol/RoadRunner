from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad_disponible = models.IntegerField(default=0)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    version = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    tipo_combustible = models.CharField(max_length=100)
    puertas = models.IntegerField()

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre


class GrupoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    productos = models.ManyToManyField(Producto, related_name='grupos')

    def __str__(self):
        return self.nombre        

