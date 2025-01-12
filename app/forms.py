from django import forms
from .models import Nome, Marca, Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'descricao', 'preco','validade', 'quantidade'] 
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
            'validade': forms.DateInput(attrs={'type': 'date'}), 
            'quantidade': forms.NumberInput() 
        }
        labels = {
            'nome':'Produto:',
            'descricao': 'Descrição:',
            'preco': 'Preço(R$):',
            'validade': 'Data de Validade:',
            'quantidade': 'Quantidade em Estoque:'
        }

class MarcaProduto(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']

        widgets = {
            'marca':forms.TextInput(attrs={'type': 'text'}),
        }
        labels = {
            'marca': 'Marca do Produto',
        }

class NomeProduto(forms.ModelForm):
    class Meta:
        model = Nome
        fields = ['nome']

        widgets = {
            'nome':forms.TextInput(attrs={'type': 'text'}),
        }

class SearchNameForm(forms.Form):
    search_term = forms.CharField(required=False, label="Pesquisar por nome")

class SearchMarkForm(forms.Form):
    search_term = forms.CharField(required=False, label="Pesquisar por marca")

class SearchPriceForm(forms.Form):
    search_term = forms.CharField(required=False, label="Pesquisar por preco")

