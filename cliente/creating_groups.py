from django.contrib.auth.models import Group

def group_create():
    customer_qs = Group.objects.filter(name='customer').exists()
    if not customer_qs:
        customer = Group(name='customer')
        customer.save()

    admin_qs = Group.objects.filter(name='admin').exists()
    if not admin_qs:
        admin = Group(name='admin')
        admin.save()