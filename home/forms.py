from django.forms import ModelForm
from pedidos.models import produtoModel

class produtoForm(ModelForm):
    class Meta:
        model = produtoModel
        fields = '__all__'