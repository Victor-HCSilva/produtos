from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from  .forms import ProdutoForm, NomeProduto, MarcaProduto
from django.db.models import Q
from .forms import SearchForm  # Importe o novo formulário
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    produto = Produto.objects.all()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Verificação de unicidade pelo nome do produto
            nome_do_produto = form.cleaned_data.get('nome')
            marca_do_produto = form.cleaned_data.get('marca')

            if Produto.objects.filter(nome=nome_do_produto).exists() and Produto.objects.filter(marca=marca_do_produto).exists():
                form.add_error('nome', 'Produto já existe.')
            else:
                form.save()
                return redirect('select_product') # Redirecione depois de salvar
    else:
        form = ProdutoForm()
    
    context = {
        "form": form,
        'produto': produto,
    }

    return render(request, 'index.html', context)

def add_product(request):
    form_nome = NomeProduto(request.POST)
    if form_nome.is_valid():
        form_nome.save()
        return redirect('index') # Redirecione depois de salvar

    context = {
        "form_name":form_nome,
    }
    return render(request, 'add_product.html', context)

def add_mark(request):
    form_marca = MarcaProduto(request.POST)
    if form_marca.is_valid():
        form_marca.save()
        return redirect('index') # Redirecione depois de salvar
    
    context = {
        "form_marca":form_marca,
    }
    return render(request, 'add_mark.html', context)

def select_product(request):
    produtos_list = Produto.objects.all()
    form = SearchForm(request.GET)

    if form.is_valid():
        search_term = form.cleaned_data.get('search_term')
        if search_term:
            produtos_list = produtos_list.filter(Q(nome__nome__icontains=search_term))

    # Configuração da paginação
    paginator = Paginator(produtos_list, 4) # 5 produtos por página
    page = request.GET.get('page')

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        # Se page não é um inteiro, exibe a primeira página
        produtos = paginator.page(1)
    except EmptyPage:
            # Se a página estiver fora do range, exibe a última página
        produtos = paginator.page(paginator.num_pages)

    context = {
        "produto": produtos,
        "form_name": form,
    }
    
    return render(request, 'select_product.html', context)

def update_product(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)  # Agora está correto!
        if form.is_valid():
            form.save()
            return redirect('select_product')
    else:
        form = ProdutoForm(instance=produto) # Use o instance para carregar os dados do model no form

    context = {
        "form": form,
        'produto': produto,
    }

    return render(request, 'update_product.html', context)

def delete_product(request, id):
    produto = get_object_or_404(Produto, id=id)  # Obtém o produto ou retorna 404
    if request.method == 'POST':  # Verifica se é um POST
       produto.delete()  # Deleta o produto
       return redirect('select_product')  # Redireciona para a lista de produtos
    
    return render(request, 'delete_product.html', {'produto':produto})