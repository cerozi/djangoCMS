# django imports
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

# current app imports
from .decorators import decorator_func
from .forms import CreateUserForm

# view to register a new user
@decorator_func
def createUserPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # creates a user instance

            user_name = form.data['username']
            user_password = form.data['password1']

            user = authenticate(request, username=user_name, password=user_password) # verifies if the user was created;
                                                                                     
            if user:
                customer = Group.objects.get(name='customer')                        # if so, add him to the customer group;
                user.groups.add(customer)

            messages.success(request, 'O user {} foi criado. '.format(user_name))
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'login/cadastro.html', context=context)


# login view
@decorator_func
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) 

        if user:
            login(request, user) # if authenticated, log the user and redirect him to his home
            return redirect('home')
        else:
            messages.info(request, 'Usúario ou senha incorretos.')


    return render(request, 'login/login.html', {})

# logout view
def logoutPage(request):

    logout(request) # logout user
    return redirect('login')

