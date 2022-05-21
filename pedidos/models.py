from django.urls import reverse
from django.db import models
from cliente.models import clienteModel

class produtoModel(models.Model):

    CATEGORIA_CHOICES = (
        ('U', 'Utensílio'),
        ('M', 'Móvel'),
        ('L', 'Lazer'),
        ('O', 'Outros'),
    )


    nome = models.CharField(max_length=50)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=1, default='O')
    preco = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome


class pedidoModel(models.Model):

    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Saiu para entrega', 'Saiu para entrega'),
        ('Entregue', 'Entregue')
    )

    produto = models.ForeignKey(produtoModel, on_delete=models.CASCADE, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=17, blank=True)
    var_cliente = models.ForeignKey(clienteModel, on_delete=models.CASCADE, verbose_name='Cliente', related_name='order')
    approved_by_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.produto.nome

    def get_approve_order_url(self):
        return reverse('pendentes-aprovar', args=(self.pk, ))

    def get_delete_order_url(self):
        return reverse('pendentes-deletar', args=(self.pk, ))