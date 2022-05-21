# django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# other apps imports
from login.decorators import decorator
from pedidos.models import pedidoModel, produtoModel
from cliente.models import clienteModel


# ADMIN HOME: here, the admin have access to a dashboard that displays all the users, orders details, 
# such as the amount of orders pending and delivered

@login_required(login_url='login')
@decorator(allowed_holes=['admin'])
def homeView(request):

    customer_list = clienteModel.objects.all()
    orders_list = pedidoModel.objects.filter(approved_by_admin=True).order_by('-data')[:5]

    # TOTAL ORDERS, ORDERS PENDING AND DELIVERED ORDERS

    delivery = pedidoModel.objects.filter(status='Entregue', approved_by_admin=True).count()
    pending = pedidoModel.objects.filter(status='Pendente', approved_by_admin=True).count()
    total_order = pedidoModel.objects.filter(approved_by_admin=True).count()

    # TOTAL OF CLIENTS

    total_clients = customer_list.count()

    # CONTEXT

    context = {
        'customers_list': customer_list,
        'orders_list': orders_list,
        'delivery': delivery,
        'pending': pending,
        'total_order': total_order,
        'total_clients': total_clients
    }

    return render(request, 'home/home.html', context=context)


# USER HOME: the customer user home allows the logged user to see all their orders, such as
# amount of each order type 

@login_required(login_url='login')
@decorator(allowed_holes=['customer'])
def userHomeView(request):

    customer_orders = request.user.customer_set.order.filter(approved_by_admin=True).order_by('-data') # queryset that
                                                                                                    # returns a list of all the
                                                                                                    # approved user orders 

    # queryset that returns that amount of each order type;
    # those amount is used to be displayed in the user dashboard

    total_orders = pedidoModel.objects.filter(var_cliente=request.user.customer_set, 
                                            approved_by_admin=True).count() 

    delivery = pedidoModel.objects.filter(var_cliente=request.user.customer_set,
                                         status='Entregue', 
                                         approved_by_admin=True).count()

    pending = pedidoModel.objects.filter(var_cliente=request.user.customer_set, 
                                        status='Pendente', 
                                        approved_by_admin=True).count()

    # context
    
    context = {
        'customer_orders': customer_orders,
        'total_orders': total_orders,
        'delivery': delivery,
        'pending': pending,
    }

    return render(request, 'home/user-home.html', context=context)
