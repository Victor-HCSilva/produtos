from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Marca, Nome
from  .forms import ProdutoForm, NomeProduto, MarcaProduto
from django.db.models import Q
from .forms import SearchNameForm, SearchMarkForm, SearchPriceForm  # Importe o novo formulário
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages 

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
    marcas = Marca.objects.all()

    if form_marca.is_valid():
        form_marca.save()
        return redirect('index') # Redirecione depois de salvar
    
    context = {
        "form_marca":form_marca,
        "marcas": marcas,

    }
    return render(request, 'add_mark.html', context)

def select_product(request):
    produtos_list = Produto.objects.all()

    for p in produtos_list:
        Warning("nome",p.nome)

    form_name = SearchNameForm(request.GET)
    form_mark = SearchMarkForm(request.GET)
    form_price = SearchPriceForm(request.GET)

    query = Q()

    if form_name.is_valid() and form_name.cleaned_data.get('search_term'):
        search_term = form_name.cleaned_data.get('search_term')
        query &= Q(nome__nome__icontains=search_term)  # Uso correto de nome__nome

    if form_mark.is_valid() and form_mark.cleaned_data.get('search_term'):
        search_term = form_mark.cleaned_data.get('search_term')
        query &= Q(marca__marca__icontains=search_term)  # Uso correto de marca__marca

    if form_price.is_valid() and form_price.cleaned_data.get('search_term'):
        search_term = form_price.cleaned_data.get('search_term')
        """try:
           search_term = float(search_term)
           query &= Q(preco=search_term)  # Use preco aqui
        except ValueError:
           pass # Se não for um número, ignora o filtro de preço"""


    if query:
        produtos_list = produtos_list.filter(query) # Aplica o filtro combinado


    # Configuração da paginação
    paginator = Paginator(produtos_list, 3)
    page = request.GET.get('page')

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    context = {
        "produto": produtos,
        "form_name": form_name,
        "form_mark": form_mark,
        "form_price": form_price,
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
    nome_produto = get_object_or_404(Nome,nome=produto.nome)

    if request.method == 'POST':  # Verifica se é um POST
       produto.delete()  # Deleta o produto
       nome_produto.delete()
       return redirect('select_product')  # Redireciona para a lista de produtos
    
    return render(request, 'delete_product.html', {'produto':produto})

def delete_mark(request, id):
    marca_produto = get_object_or_404(Marca, id=id)  # Obtém a marca ou retorna 404

    try:
        # Tenta encontrar um produto que utilize esta marca
        yet_using_mark = Produto.objects.filter(marca=marca_produto).first()
    except Produto.DoesNotExist:
        yet_using_mark = None
    
    if yet_using_mark:
        # Se a marca estiver em uso, adiciona uma mensagem de erro
        messages.error(request, "Esta marca ainda está em uso por um ou mais produtos e não pode ser deletada.")
        return render(request, 'delete_mark.html', {'mark': marca_produto})

    if request.method == 'POST':
        marca_produto.delete()  # Deleta o produto
        messages.success(request, "Marca deletada com sucesso!") # Mensagem de sucesso
        return redirect('index')  # Redireciona para a lista de produtos

    return render(request, 'delete_mark.html', {'mark': marca_produto})

def update_mark(request, id):
    marca = get_object_or_404(Marca, id=id)

    if request.method == 'POST':
        form = MarcaProduto(request.POST, instance=marca)  # Agora está correto!
        if form.is_valid():
            form.save()
            return redirect('add_mark')
    else:
        form = MarcaProduto(instance=marca) # Use o instance para carregar os dados do model no form

    context = {
        "form": form,
        'marca': marca,
    }

    return render(request, 'update_mark.html', context)

