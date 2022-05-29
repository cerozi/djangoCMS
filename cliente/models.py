from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import Group


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
        
        num = pedidoModel.objects.filter(var_cliente=self, approved_by_admin=True).count()
        return num

    def __str__(self):
        return self.nome


# django signals; receiver that creates a client model and adds user to the 'customer' group
def create_customer_profile(sender, instance, created, **kwargs):
    if created:

        if not instance.is_staff:
            group = Group.objects.filter(name='customer')
            if group.exists():
                instance.groups.add(group[0])

            clienteModel.objects.create(user=instance, nome=instance.username)
        else:
            group = Group.objects.filter(name='admin')
            if group.exists():
                instance.groups.add(group[0])
    


post_save.connect(create_customer_profile, sender=User)