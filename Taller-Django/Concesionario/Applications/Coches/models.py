from django.db import models
from Applications.Clientes.models import Clientes
from django.urls import reverse

class Coches_Vendidos(models.Model):

    matricula=models.CharField(max_length=10)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    precio=models.IntegerField()
    extras_instalados=models.CharField(max_length=20)
    codigo_cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    numero_puertas=models.IntegerField()

    def get_absolute_url(self): 
        return reverse('listar_coches_vendidos')

    def __str__(self):
        return self.matricula 

class Revisiones(models.Model):

    cambio_aceite=models.CharField(max_length=2)
    cambio_filtro=models.CharField(max_length=2)
    revision_frenos=models.CharField(max_length=2)
    otros=models.CharField(max_length=255)
    matricula=models.ForeignKey(Coches_Vendidos, on_delete=models.CASCADE)

    def get_absolute_url(self): 
        return reverse('listar_revisiones')

    def __str__(self):
        return str(self.matricula)

