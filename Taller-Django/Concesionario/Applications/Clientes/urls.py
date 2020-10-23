from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('listar_clientes/', views.Listar_Clientes.as_view(), name='listar_clientes'),
    path('crear_cliente/', views.Crear_Cliente.as_view(), name="crear_cliente"),
    path('actualizar_cliente/<pk>', views.Actualiza_Cliente.as_view(), name="actualizar_cliente")

]