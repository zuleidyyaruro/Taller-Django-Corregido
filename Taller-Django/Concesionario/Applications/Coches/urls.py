from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('coches-vendidos/', views.Listar_Coches_Vendidos.as_view(), name='listar_coches_vendidos'),
    path('crear-coches-vendido/', views.Crear_Coches_Vendido.as_view(), name='crear_coche_vendido'),
    path('actualizar-coches-vendido/<pk>', views.Actualiza_Coche_Vendido.as_view(), name='actualizar_coches_vendidos'),
    
     
    path('revisiones/', views.Listar_Revisiones.as_view(), name='listar_revisiones'),
    path('crear-revision/', views.Crear_Revision.as_view(), name='crear_revision'),
    path('actualizar-revision/<pk>', views.Actualizar_Revision.as_view(), name='actualizar_revisiones')
]