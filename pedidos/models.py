from django.db import models
from cliente.models import clienteModel

# Create your models here.

class produtoModel(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class pedidoModel(models.Model):

    status_choices = (
        ('Pendente', 'Pendente'),
        ('Saiu para entrega', 'Saiu para entrega'),
        ('Entregue', 'Entregue')
    )

    produto = models.ForeignKey(produtoModel, on_delete=models.CASCADE, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=17, blank=True)
    var_cliente = models.ForeignKey(clienteModel, on_delete=models.CASCADE, verbose_name='Cliente', related_name='order')

    def __str__(self):
        return self.produto.nome
