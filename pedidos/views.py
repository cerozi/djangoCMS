from django.views.generic import ListView
from django.shortcuts import redirect, render
from .forms import pedidoFormAdmin, pedidoFormUser
from django.urls import reverse
from .models import pedidoModel
from cliente.models import clienteModel

from django.contrib.auth.decorators import login_required
from login.decorators import decorator

from django.utils.decorators import method_decorator


# Create your views here.

# ========= ADMIN ========

# CRIAR PEDIDO

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def pedidoCreate(request):
    form = pedidoFormAdmin()
    if request.method == 'POST':
        form = pedidoFormAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Criar pedido:',
        'botao': 'Cadastrar'
    }

    return render(request, 'pedidos/criar-editar-pedido.html', context=context)

# EDITAR PEDIDO

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def pedidoUpdate(request, pk):
    order = pedidoModel.objects.get(pk=pk)
    form = pedidoFormAdmin(instance=order)

    if request.method == 'POST':
        form = pedidoFormAdmin(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Editar pedido',
        'botao': 'Editar',
    }

    return render(request, 'pedidos/criar-editar-pedido.html', context=context)

# DELETAR PEDIDO

@login_required(login_url='login')  
@decorator(allowed_holes=['admin'])
def pedidoDelete(request, pk):
    order = pedidoModel.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect(reverse('home'))

    context = {
        'order': order
    }

    return render(request, 'pedidos/deletar-pedido.html', context=context)

# PEDIDOS PENDENTES 

class pedidosPendentes(ListView):
    template_name = 'pedidos/pedidos-pendentes.html'

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, *args, **kwargs):
        orders_pending = pedidoModel.objects.filter(approved_by_admin=False)

        return render(request, 'pedidos/pedidos-pendentes.html', {'orders_pending': orders_pending})

@decorator(allowed_holes=['admin'])
def pedidosPendentesApprove(request, pk):
    if request.method == 'POST':
        pedido = pedidoModel.objects.get(pk=pk)
        pedido.approved_by_admin = True
        pedido.save()

    return redirect(reverse('pendentes'))

@decorator(allowed_holes=['admin'])
def pedidosPendentesDelete(request, pk):
    if request.method == 'POST':
        pedido = pedidoModel.objects.get(pk=pk)
        pedido.delete()

    return redirect(reverse('pendentes'))

# ========= USER ========

def pedidoCreateUser(request):
    form = pedidoFormUser()

    if request.method == 'POST':
        form = pedidoFormUser(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            user = clienteModel.objects.get(user=request.user)

            pedido_instance = pedidoModel(produto=produto, var_cliente=user, approved_by_admin=False, status='Pendente')
            pedido_instance.save()

            return redirect(reverse('home'))
    
    return render(request, 'pedidos/criar-editar-pedido.html', {'form': form, 'titulo': 'Solicitar Pedido', 'botao': 'Solicitar'})