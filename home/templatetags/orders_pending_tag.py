from django import template
from pedidos.models import pedidoModel

register = template.Library()

@register.simple_tag
def orders_pending():
    return pedidoModel.objects.filter(approved_by_admin=False).count()