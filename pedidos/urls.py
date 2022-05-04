from django.urls import path
from .views import pedidoCreate, pedidoUpdate, pedidoDelete, pedidoCreateUser, pedidosPendentes, pedidosPendentesApprove, pedidosPendentesDelete


urlpatterns = [
    # ==== ADMIN ===
    # // CRUD de pedidos
    path('criar-pedido/', pedidoCreate, name='criar-pedido'),
    path('editar-pedido/<int:pk>', pedidoUpdate, name='editar-pedido'),
    path('deletar-pedido/<int:pk>', pedidoDelete, name='deletar-pedido'),

    # // aprovação, exclusão e leitura de pedidos pendentes
    path('pendentes/', pedidosPendentes.as_view(), name='pendentes'),
    path('pendentes/aprovar/<int:pk>', pedidosPendentesApprove, name='pendentes-aprovar'),
    path('pendentes/deletar/<int:pk>', pedidosPendentesDelete, name='pendentes-deletar'),

    # ==== USER ===
    path('user/solicitar-pedido/', pedidoCreateUser, name='solicitar-pedido'),
]