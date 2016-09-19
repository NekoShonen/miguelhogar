from django.db import models

class Producto(models.Model):
    codigoDeBarras = models.IntegerField()
    nombre = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey('Marca')
    precio = models.CharField(max_length=20)
    rubro = models.CharField(max_length=200)
    proveedor = models.ForeignKey('Proveedor')

    def __str__(self):
        return self.nombre + ' ' + self.modelo + ' ' + self.marca.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    celular = models.IntegerField()
    marcaDistribuye = models.ForeignKey('Marca')

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre