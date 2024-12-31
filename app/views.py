from django.shortcuts import render
from .models import Produto
from  .forms import ProdutoForm
# Create your views here.
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