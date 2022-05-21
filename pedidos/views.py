# django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView

# other apps imports
from login.decorators import decorator
from cliente.models import clienteModel

# current apps imports
from .forms import pedidoFormAdmin, pedidoFormUser
from .models import pedidoModel


# === ADMIN ORDER VIEWS === 
# views that allow the admin to CRUD the orders;


# create order view
@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def pedidoCreate(request):
    form = pedidoFormAdmin()
    if request.method == 'POST':
        form = pedidoFormAdmin(request.POST)
        if form.is_valid():
            form.save() # creates a new order instance
            messages.info(request, "Pedido criado. ")
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Criar pedido:',
        'botao': 'Cadastrar'
    }

    return render(request, 'pedidos/criar-editar-pedido.html', context=context)

# update order
@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def pedidoUpdate(request, pk):
    order = pedidoModel.objects.get(pk=pk)
    form = pedidoFormAdmin(instance=order)

    if request.method == 'POST':
        form = pedidoFormAdmin(request.POST, instance=order)
        if form.is_valid():
            form.save() # updates a order instance
            messages.info(request, "Pedido atualizado. ")
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Editar pedido',
        'botao': 'Editar',
    }

    return render(request, 'pedidos/criar-editar-pedido.html', context=context)

# deletes order
@login_required(login_url='login')  
@decorator(allowed_holes=['admin'])
def pedidoDelete(request, pk):
    order = pedidoModel.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete() # deletes a order instance
        messages.info(request, "Pedido excluído. ")
        return redirect(reverse('home'))

    context = {
        'object': order
    }

    return render(request, 'pedidos/deletar-pedido.html', context=context)

# ___ pending orders ____
# pending orders are orders that were requested by the client and are waiting for the admin approval;


# lists all the pending orders
class pedidosPendentes(ListView):
    template_name = 'pedidos/pedidos-pendentes.html'

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, *args, **kwargs):
        orders_pending = pedidoModel.objects.filter(approved_by_admin=False)

        return render(request, 'pedidos/pedidos-pendentes.html', {'orders_pending': orders_pending})

# approve the pending order
@decorator(allowed_holes=['admin'])
def pedidosPendentesApprove(request, pk):
    if request.method == 'POST':
        pedido = pedidoModel.objects.get(pk=pk)
        pedido.approved_by_admin = True
        pedido.save()
        messages.info(request, "Solicitação de pedido aprovada. ")

    return redirect(reverse('pendentes'))

# deny the pending order
@decorator(allowed_holes=['admin'])
def pedidosPendentesDelete(request, pk):
    if request.method == 'POST':
        pedido = pedidoModel.objects.get(pk=pk)
        pedido.delete()
        messages.info(request, "Solicitação de pedido reprovada. ")

    return redirect(reverse('pendentes'))

# === USER VIEWS ===
# allow user to request a new order; admin can approve or deny the request order;

def pedidoCreateUser(request):
    form = pedidoFormUser()

    if request.method == 'POST':
        form = pedidoFormUser(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            user = clienteModel.objects.get(user=request.user)

            pedido_instance = pedidoModel(produto=produto, var_cliente=user, approved_by_admin=False, status='Pendente')
            pedido_instance.save() # creates order instance

            messages.info(request, "Solicitação de pedido realizada. Aguardar aprovação do admin. ")
            return redirect(reverse('home'))
    
    return render(request, 'pedidos/criar-editar-pedido.html', {'form': form, 'titulo': 'Solicitar Pedido', 'botao': 'Solicitar'})
