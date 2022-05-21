# django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

# other apps imports
from login.decorators import decorator
from pedidos.models import pedidoModel

# current app imports
from .forms import clienteForm, orderFilter, userProfileForm
from .models import clienteModel


# ==== ADMIN VIEWS ===
# Basically, these views set the permission the admin to create, update, delete, and get the detail
# from a client model

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def clienteCreate(request):
    form = clienteForm()
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Cliente criado com sucesso. ")
            return redirect(reverse('home'))

    context = {
        'form': form,
        'titulo': 'Criar cliente',
        'botao': 'Cadastrar',
    }

    return render(request, 'cliente/admin/criar-cliente.html', context=context)


@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
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
@decorator(allowed_holes=['admin'])
def updateClienteProfile(request, slug):
    template_name = 'cliente/user/profile.html'
    cliente = clienteModel.objects.get(slug=slug)

    if request.method == 'POST':
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid() and request.user.is_staff:
            form.save()
            messages.info(request, 'Perfil atualizado ({}).'.format(cliente.nome))
            return redirect(reverse('perfil-cliente', args=(cliente.slug, )))

    form = clienteForm(instance=cliente)

    return render(request, template_name, {'form': form})

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def deleteClienteModel(request, slug):
    template_name = 'pedidos/deletar-pedido.html'
    cliente = clienteModel.objects.get(slug=slug)

    if request.method == 'POST':
        cliente.delete()
        messages.info(request, 'Perfil deletado ({}).'.format(cliente.nome))
        return redirect(reverse('home'))


    return render(request, template_name, {'object': cliente})

# == CUSTOMER/REGULAR USER VIEWS ==
# regular users can only have access to their profile
# this view can get bot GET and HTTP methods: with get method user see the detail from their client profile
# with POST method, they can update their profile

@login_required(login_url='login')
@decorator(allowed_holes=['customer'])
def userProfile(request):
    
    customer_user = clienteModel.objects.get(user=request.user)
    form = userProfileForm(instance=customer_user)

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES, instance=customer_user)
        if form.is_valid():
            form.save()
            messages.info(request, "Perfil atualizado. ")
            redirect('user')

    context = {
        'form': form
    }

    return render(request, 'cliente/user/profile.html', context=context)

