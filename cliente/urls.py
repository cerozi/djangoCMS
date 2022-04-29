from django.urls import path
from .views import clienteDetail, clienteCreate, userProfile

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cliente/<slug:slug>', clienteDetail, name='perfil-cliente'),
    path('criar-cliente/', clienteCreate, name='criar-cliente'),
    path('perfil/', userProfile, name='perfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)