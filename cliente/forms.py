from django.forms import ModelForm

from pedidos.models import pedidoModel
from .models import clienteModel

# CADASTRO DE CLIENTES PELO ADMIN/STAFF

class clienteForm(ModelForm):
    class Meta:
        model = clienteModel
        fields = ('nome', 'email', 'tel')

# FILTRO DE PESQUISA DE PEDIDOS 

class orderFilter(ModelForm):
    class Meta:
        model = pedidoModel
        fields = ('produto', 'status')

# EDIÇÃO DO PERFIL DO USÚARIO LOGADO

class userProfileForm(ModelForm):
    class Meta:
        model = clienteModel
        fields = '__all__'
        exclude = ['user', 'slug']