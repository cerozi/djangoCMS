from django.shortcuts import get_object_or_404, render, redirect
from cliente.models import clienteModel
from pedidos.models import pedidoModel, produtoModel

from django.contrib.auth.decorators import login_required
from login.decorators import decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator

from .forms import produtoForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

# == HOME ==

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def homeView(request):

    customer_list = clienteModel.objects.all()
    orders_list = pedidoModel.objects.filter(approved_by_admin=True).order_by('-data')[:5]

    # PEDIDOS ENTREGUES, PENDENTES E TOTAL

    delivery = pedidoModel.objects.filter(status='Entregue', approved_by_admin=True).count()
    pending = pedidoModel.objects.filter(status='Pendente', approved_by_admin=True).count()
    total_order = pedidoModel.objects.filter(approved_by_admin=True).count()

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

    customer_orders = request.user.customer_set.order.filter(approved_by_admin=True).order_by('-data')

    total_orders = pedidoModel.objects.filter(var_cliente=request.user.customer_set, 
                                            approved_by_admin=True).count()

    delivery = pedidoModel.objects.filter(var_cliente=request.user.customer_set,
                                         status='Entregue', 
                                         approved_by_admin=True).count()

    pending = pedidoModel.objects.filter(var_cliente=request.user.customer_set, 
                                        status='Pendente', 
                                        approved_by_admin=True).count()

    context = {
        'customer_orders': customer_orders,
        'total_orders': total_orders,
        'delivery': delivery,
        'pending': pending,
    }

    return render(request, 'home/user-home.html', context=context)

# === PRODUTOS ===

class productsList(ListView):
    template_name = 'home/produtos.html'

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, *args, **kwargs):
        
        produtos = produtoModel.objects.all()

        return render(request, self.template_name, {'produtos': produtos})

class productCreate(CreateView):
    template_name = 'pedidos/criar-editar-pedido.html'

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, *args, **kwargs):
        form = produtoForm()

        return render(request, self.template_name, {'form': form, 'titulo': 'Criar produto', 'botao': 'Registrar'})

    @method_decorator(decorator(allowed_holes=['admin']))
    def post(self, request, *args, **kwargs):
        form = produtoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Produto criado com sucesso. ")
            return redirect(reverse('products'))
        
        else:
            return render(request, self.template_name, {'form': form, 'titulo': 'Criar produto', 'botao': 'Registrar'})

class productUpdate(UpdateView):
    template_name = 'pedidos/criar-editar-pedido.html'

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, pk, *args, **kwargs):
        produto = produtoModel.objects.get(pk=pk)
        form = produtoForm(instance=produto)

        return render(request, self.template_name, {'form': form, 'botao': 'Editar', 'titulo': 'Editar pedido'})

    @method_decorator(decorator(allowed_holes=['admin']))
    def post(self, request, pk, *args, **kwargs):
        produto = produtoModel.objects.get(pk=pk)
        form = produtoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.info(request, 'Produto atualizado. ')
            return redirect(reverse('products'))
        else:
            messages.info(request, 'Formulário inválido. ')
            return redirect(reverse('editar-produto', args=(produto.pk, )))

class productDelete(DeleteView):

    @method_decorator(decorator(allowed_holes=['admin']))
    def get(self, request, *args, **kwargs):
        return redirect(reverse('products'))

    @method_decorator(decorator(allowed_holes=['admin']))
    def post(self, request, pk, *args, **kwargs):
        produto = get_object_or_404(produtoModel, pk=pk)
        produto.delete()

        messages.info(request, 'Produto excluído. ')
        return redirect(reverse('products'))