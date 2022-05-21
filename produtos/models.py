from django.db import models

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