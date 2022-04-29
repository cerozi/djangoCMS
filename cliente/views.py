from itertools import product
from django.shortcuts import render, redirect
from .models import clienteModel
from pedidos.models import pedidoModel
from .forms import clienteForm, orderFilter
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from login.decorators import decorator

from .forms import userProfileForm

# Create your views here.

@login_required(login_url='login')
def clienteCreate(request):
    form = clienteForm()
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Criar cliente',
        'botao': 'Cadastrar',
    }

    return render(request, 'cliente/admin/criar-cliente.html', context=context)


@login_required(login_url='login')
def clienteDetail(request, slug):

    form = orderFilter()

    customer = clienteModel.objects.get(slug=slug)
    customer_orders = pedidoModel.objects.filter(var_cliente=customer)
    customer_orders_count = pedidoModel.objects.filter(var_cliente=customer).count()

    # FILTRO DE PESQUISA

    product_selected = request.GET.get('produto')
    status_selected = request.GET.get('status')

    if product_selected and status_selected == "":
        customer_orders = pedidoModel.objects.filter(var_cliente=customer, produto=product_selected)
    elif status_selected and product_selected == "":
        customer_orders = pedidoModel.objects.filter(var_cliente=customer, status=status_selected)
    elif status_selected and product_selected:
        customer_orders = pedidoModel.objects.filter(var_cliente=customer, status=status_selected, produto=product_selected)
    else:
        customer_orders = pedidoModel.objects.filter(var_cliente=customer)
    # ==================================

    context = {
        'customer': customer,
        'customer_orders': customer_orders,
        'customer_orders_count': customer_orders_count,
        'form': form,
    }

    return render(request, 'cliente/admin/cliente.html', context=context)

@login_required(login_url='login')
@decorator(allowed_holes=['customer'])
def userProfile(request):
    
    customer_user = clienteModel.objects.get(user=request.user)
    form = userProfileForm(instance=customer_user)

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES, instance=customer_user)
        if form.is_valid():
            form.save()
            redirect('user')

    context = {
        'form': form
    }

    return render(request, 'cliente/user/profile.html', context=context)