from django.shortcuts import redirect, render
from .forms import pedidoForm
from django.urls import reverse
from .models import pedidoModel

from django.contrib.auth.decorators import login_required
from login.decorators import decorator


# Create your views here.


# CRIAR PEDIDO


@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def pedidoCreate(request):
    form = pedidoForm()
    if request.method == 'POST':
        form = pedidoForm(request.POST)
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
    form = pedidoForm(instance=order)

    if request.method == 'POST':
        form = pedidoForm(request.POST, instance=order)
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