from django.shortcuts import render
from .models import Coches_Vendidos, Revisiones

from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.

class Listar_Coches_Vendidos(ListView):
    template_name = "cochesVendidos/listar_coches_vendidos.html"
    model=Coches_Vendidos
    context_object_name='lista'

class Crear_Coches_Vendido(CreateView):

    template_name="cochesVendidos/crear_coche_vendido.html"
    model=Coches_Vendidos
    fields=['matricula', 'marca', 'modelo', 'color', 'precio', 'extras_instalados', 'codigo_cliente', 'numero_puertas']

class Actualiza_Coche_Vendido(UpdateView):
    
    template_name="cochesVendidos/actualizar_coche_vendido.html"
    model=Coches_Vendidos
    fields=['matricula', 'marca', 'modelo', 'color', 'precio', 'extras_instalados', 'codigo_cliente', 'numero_puertas']


class Listar_Revisiones(ListView):
    template_name = "revisiones/listar_revisiones.html"
    model=Revisiones
    context_object_name='lista'

class Crear_Revision(CreateView):

    template_name="revisiones/crear_revision.html"
    model=Revisiones
    fields=['cambio_aceite', 'cambio_filtro', 'revision_frenos', 'otros', 'matricula']

class Actualizar_Revision(UpdateView):
    
    template_name="revisiones/actualizar_revision.html"
    model=Revisiones
    fields=['cambio_aceite', 'cambio_filtro', 'revision_frenos', 'otros', 'matricula']