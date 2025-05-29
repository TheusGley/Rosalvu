from django.db import models
from django.contrib.auth.models import User ,AbstractUser

class Cliente (models.Model):
    nome = models.CharField(max_length=100,null=False)
    data_nasc = models.DateField(auto_now=False,null=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    ultima_entrada = models.DateField(auto_now=False,null=True)
    notas = models.CharField(max_length=100,blank=True, null=True)
    

    
    def __str__(self):
        return self.nome
    
servicos_choices = [
("Disponivel", "Disponivel"),
("Indisponivel", "Indisponivel"),

    
]  
    
class Servico (models.Model):
    
    nome_servico =  models.CharField(max_length=100)
    colaborador = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'servico_colaborador')
    status = models.CharField(max_length=20, choices= servicos_choices)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    notas = models.CharField(max_length=100, blank=True, null=True) 
    
    
    def __str__(self) :
        return self.nome_servico 
    
class Vendas (models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data  = models.DateField(auto_now=False,null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.cliente.nome
    

class Carrinho (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank = True)
    total = models.PositiveIntegerField(default=0)
    data_criado = models.DateField(auto_now_add=True)
    
    def  __str__(self) :
        
        return "Carrinho"  + str(self.id)

class Produto_Carrinho (models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    subtotal = models.PositiveIntegerField()
    
    def  __str__(self) :
        
        return "Carrinho: " + str(self.carrinho.id) + "   Produto: "+ str(self.id)
    

    
class Pedidos (models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    
    def __str__(self):
        return  "Pedidos " + str(self.id)
    