from django.forms import ModelForm
from .models import pedidoModel

class pedidoForm(ModelForm):
    class Meta:
        model = pedidoModel
        fields = ('produto', 'var_cliente', 'status')