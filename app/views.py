from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from  .forms import ProdutoForm
from .forms import NomeProduto

def index(request):
    produto = Produto.objects.all()
    form = ProdutoForm(request.POST)

    if form.is_valid():
        form.save()
        
    context = {
        "produto":produto,
        'form':form,
    }

    return render(request, 'index.html', context)

def add_product(request):
    form_nome = NomeProduto(request.POST)
    if form_nome.is_valid():
        form_nome.save()

    context = {
        "form_name":form_nome,
    }
    return render(request, 'add_product.html', context)


def select_product(request):
    produtos = Produto.objects.all()
    form_nome = NomeProduto(request.POST)

    if form_nome.is_valid():
        form_nome.save()

    context = {
        "produto":produtos,
        "form_name":form_nome,
    }
    
    return render(request, 'select_product.html', context)

def update_product(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)  # Agora está correto!
        if form.is_valid():
            form.save()
            return redirect('nome_da_view_detalhe_do_produto', id=id)
    else:
        form = ProdutoForm(instance=produto) # Use o instance para carregar os dados do model no form

    context = {
        "form": form,
        'produto': produto,
    }
    return render(request, 'update_product.html', context)