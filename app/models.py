from django.db import models

class Nome(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca
    
class Produto(models.Model):
    nome = models.ForeignKey(Nome, on_delete=models.SET_NULL, blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, blank=True, null=True) 
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Campo para o preço
    validade = models.DateField(null=True, blank=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome