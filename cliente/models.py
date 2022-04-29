from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.contrib.auth.models import Group

# Create your models here.

class clienteModel(models.Model):
    photo = models.ImageField(default='default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_set')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=11)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.nome, allow_unicode=True)

        return super().save()

    def num_pedidos(self):

        from pedidos.models import pedidoModel
        
        num = pedidoModel.objects.filter(var_cliente=self).count()
        return num

    def __str__(self):
        return self.nome


# DJANGO SIGNALS PARA CRIAÇÃO AUTOMÁTICA DE PERFIL

def criaProfile(sender, instance, created, **kwargs):
    if created:

        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        clienteModel.objects.create(user=instance, nome=instance.username)
        print('Signal chamado com sucesso. ')

    

post_save.connect(criaProfile, sender=User)
