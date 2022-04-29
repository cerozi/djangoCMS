from django.contrib import admin
from .models import pedidoModel, produtoModel

# Register your models here.
admin.site.register(pedidoModel)
admin.site.register(produtoModel)

