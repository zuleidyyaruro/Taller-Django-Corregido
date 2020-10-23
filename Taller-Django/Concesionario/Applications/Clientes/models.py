from django.db import models
from django.urls import reverse

# Create your models here.
class Clientes(models.Model):
  
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    departamento=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=100)
    codigo_postal=models.CharField(max_length=6)
    telefono=models.CharField(max_length=10)
    fecha_nacimiento=models.DateField()

    def get_absolute_url(self): 
        return reverse('listar_clientes')

    def __str__(self):
        return self.nombres + "-" + self.apellidos