from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="id de categoria")
    nombreCategoria = models.CharField(max_length=200, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, verbose_name="Patente del vehículo" )
    marca =  models.CharField(max_length=20, verbose_name="Marca del vehículo")
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name="Modelo del vehículo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
