# django imports
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# other apps imports
from login.decorators import decorator

# current app imports
from .forms import produtoForm
from .models import produtoModel


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
