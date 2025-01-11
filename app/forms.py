from django import forms
from .models import Produto
from .models import Nome

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'validade', 'quantidade']  # Campos que aparecerão no formulário
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
            'validade': forms.DateInput(attrs={'type': 'date'}), # Widget para data
            'quantidade': forms.NumberInput() # Widget para quantidade
        }
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição do Produto',
            'preco': 'Preço do Produto (R$)',
            'validade': 'Data de Validade',
             'quantidade': 'Quantidade em Estoque'
        }
class NomeProduto(forms.ModelForm):
    class Meta:
        model = Nome
        fields = ['nome']

        widgets = {
            'nome':forms.TextInput(attrs={'type': 'text'}),
        }
        labels = {
            'nome': 'Nome do Produto',
        }