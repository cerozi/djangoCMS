from django.forms import ModelForm
from .models import pedidoModel

class pedidoFormAdmin(ModelForm):
    class Meta:
        model = pedidoModel
        fields = ('produto', 'var_cliente', 'status')

class pedidoFormUser(ModelForm):
    class Meta:
        model = pedidoModel
        fields = ('produto', )