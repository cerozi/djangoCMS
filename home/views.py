from django.shortcuts import render, redirect
from cliente.models import clienteModel
from pedidos.models import pedidoModel

from django.contrib.auth.decorators import login_required
from login.decorators import decorator

# Create your views here.


@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def homeView(request):

    customer_list = clienteModel.objects.all()
    orders_list = pedidoModel.objects.all().order_by('-data')[:5]

    # PEDIDOS ENTREGUES, PENDENTES E TOTAL

    delivery = pedidoModel.objects.filter(status='Entregue').count()
    pending = pedidoModel.objects.filter(status='Pendente').count()
    total_order = pedidoModel.objects.all().count()

    # TOTAL DE CLIENTES

    total_clients = customer_list.count()

    # CONTEXTO

    context = {
        'customers_list': customer_list,
        'orders_list': orders_list,
        'delivery': delivery,
        'pending': pending,
        'total_order': total_order,
        'total_clients': total_clients
    }

    return render(request, 'home/home.html', context=context)


@login_required(login_url='login')
@decorator(allowed_holes=['customer'])
def userHomeView(request):

    customer_orders = request.user.customer_set.order.all()

    total_orders = pedidoModel.objects.filter(var_cliente=request.user.customer_set).count()
    delivery = pedidoModel.objects.filter(var_cliente=request.user.customer_set, status='Entregue').count()
    pending = pedidoModel.objects.filter(var_cliente=request.user.customer_set, status='Pendente').count()

    context = {
        'customer_orders': customer_orders,
        'total_orders': total_orders,
        'delivery': delivery,
        'pending': pending,
    }

    return render(request, 'home/user-home.html', context=context)