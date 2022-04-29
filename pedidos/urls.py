from django.urls import path
from .views import pedidoCreate, pedidoUpdate, pedidoDelete


urlpatterns = [
    path('criar-pedido/', pedidoCreate, name='criar-pedido'),
    path('editar-pedido/<int:pk>', pedidoUpdate, name='editar-pedido'),
    path('deletar-pedido/<int:pk>', pedidoDelete, name='deletar-pedido')
]