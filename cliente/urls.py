from django.urls import path
from .views import clienteDetail, clienteCreate, userProfile, updateClienteProfile, deleteClienteModel

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # CRUD operations from the ADMIN
    path('cliente/<slug:slug>', clienteDetail, name='perfil-cliente'),
    path('cliente/<slug:slug>/editar/', updateClienteProfile, name='editar-cliente'),
    path('cliente/<slug:slug>/deletar/', deleteClienteModel, name='deletar-cliente'),
    path('criar-cliente/', clienteCreate, name='criar-cliente'),

    # logged CUSTOMER profile 
    path('perfil/', userProfile, name='perfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)