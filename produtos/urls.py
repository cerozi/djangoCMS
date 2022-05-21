from django.urls import path
from .views import productDelete, productsList, productCreate, productUpdate

urlpatterns = [
    path('produtos/', productsList.as_view(), name='products'),
    path('produtos/criar/', productCreate.as_view(), name='criar-produto'),
    path('produtos/editar/<int:pk>/', productUpdate.as_view(), name='editar-produto'),
    path('produtos/excluir/<int:pk>/', productDelete.as_view(), name='excluir-produto'),
]