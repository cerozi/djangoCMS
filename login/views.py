from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .decorators import decorator_func

# Create your views here.

def createUserPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.data['username']
            messages.success(request, 'O user {} foi criado. '.format(user_name))
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'login/cadastro.html', context=context)



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usúario ou senha incorretos.')


    return render(request, 'login/login.html', {})

def logoutPage(request):

    logout(request)
    return redirect('login')
