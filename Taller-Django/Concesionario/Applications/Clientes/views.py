from django.shortcuts import render, redirect
from .models import Clientes

from django.views.generic import ListView, CreateView, TemplateView, UpdateView

class Listar_Clientes(ListView):
    
    template_name = "clientes/listar_clientes.html"
    model=Clientes
    context_object_name='lista'

class Crear_Cliente(CreateView):

    template_name="clientes/crear_cliente.html"
    model=Clientes
    fields=['nombres', 'apellidos', 'direccion', 'departamento', 'ciudad', 'codigo_postal', 'telefono', 'fecha_nacimiento' ]

class Actualiza_Cliente(UpdateView):
    
    template_name="clientes/actualizar_cliente.html"
    model=Clientes
    fields=['nombres', 'apellidos', 'direccion', 'departamento', 'ciudad', 'codigo_postal', 'telefono', 'fecha_nacimiento' ]
