from django.shortcuts import render, redirect
from .models import *
import datetime
from django.db.models import Count, Sum
from .useraccess import *
from django.db.models.functions import TruncMonth
def homeView(request):
    
    return render(request,"site\index.html") 

def homeSystemView(request):
    
    is_mobile(request)    
    
    if is_mobile(request):
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "home"
        mobile = "true"
        
        
        context = {'clientes':clientes,
                   'active':active,
                'mobile':mobile,
                'servicos':servicos,
               }
        return  render(request,"sistema\homeCel.html", context)  
    else:
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "home"
        
        context = {'clientes':clientes,
                'servicos':servicos,
                'active':active}
        
        return render(request,"sistema\home.html", context) 
    




def calendarioView(request):
    is_mobile(request)    
    
    if is_mobile(request):
        mobile = "true"
        
        clientes = Cliente.objects.all()
        active = "calendario"
        context = {'clientes':clientes,
                'mobile':mobile,
               'active':active
               }
        return render(request,"sistema\calendario.html", context) 
    
    else:
        clientes = Cliente.objects.all()
        active = "calendario"
        context = {'clientes':clientes,
               'active':active
               }
    
    return render(request,"sistema\calendario.html", context) 


def clientesView(request):
    
    if is_mobile(request):
        mobile = "true"
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "clientes"
        context = {'clientes':clientes,
                'mobile':mobile,
                'servicos':servicos,
                'active':active
                }
        
        return render(request,"sistema\clientes.html", context) 
    else:
        
    
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "clientes"
        context = {'clientes':clientes,
                'servicos':servicos,
                'active':active
                }
        
        return render(request,"sistema\clientes.html", context) 

def servicosView(request):
    
    if is_mobile(request):
        mobile = "true"
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "servicos"
        context = {'clientes':clientes,
                'mobile':mobile,
               'servicos':servicos,
               'active':active
               }
    
        return render(request,"sistema\servicos.html", context) 
    
    else:
    
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "servicos"
        context = {'clientes':clientes,
                'servicos':servicos,
                'active':active
                }
        
        return render(request,"sistema\servicos.html", context) 




def atividadesView(request):
    
    if is_mobile(request):
        mobile = "true"
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "servicos"
        context = {'clientes':clientes,
                'mobile':mobile,
                'servicos':servicos,
                'active':active
                }
        
        return render(request,"sistema\servicos.html", context) 
        
    else:
    
        clientes = Cliente.objects.all()
        servicos = Servico.objects.all()
        active = "servicos"
        context = {'clientes':clientes,
                'servicos':servicos,
                'active':active
                }
        
    return render(request,"sistema\servicos.html", context) 



def movimentacaoView(request):
    hoje = datetime.date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    mes_atual_STR = hoje.strftime("%B").capitalize()

    if is_mobile(request):
        mobile = "true"
        active = "vendas"
        
        from collections import defaultdict
        active = "vendas"
        from django.db.models import Sum
        
        vendas_mes_atual = Vendas.objects.filter(data__month=mes_atual)
        vendas_total = Vendas.objects.all()


        vendas_por_mes_dict = defaultdict(list)

        for v in vendas_total:
            mes = v.data.strftime('%Y-%m')  
            vendas_por_mes_dict[mes].append(v.valor)

        vendas_por_mes = [
            {'mes': mes, 'total': sum(valores)}
            for mes, valores in vendas_por_mes_dict.items()
            ]
        total_vendas = vendas_total.aggregate(total=Sum("valor"))["total"]   
        print(vendas_por_mes)
        
        context = {
            'antes': Cliente.objects.all(),
            'servicos': Servico.objects.all(),
            'active': active,
            'mes_atual': mes_atual_STR, 
            'vendas_mes_atual': vendas_mes_atual,
            'total_vendas':total_vendas,
            'vendas_mes': vendas_por_mes,
            'mobile':  mobile 
        }
        

        return render(request, "sistema/movimentacao.html", context)
    else:
        from collections import defaultdict
        active = "vendas"
        from django.db.models import Sum
        
        vendas_mes_atual = Vendas.objects.filter(data__month=mes_atual)
        vendas_total = Vendas.objects.all()


        vendas_por_mes_dict = defaultdict(list)

        for v in vendas_total:
            mes = v.data.strftime('%Y-%m')  
            vendas_por_mes_dict[mes].append(v.valor)

        vendas_por_mes = [
            {'mes': mes, 'total': sum(valores)}
            for mes, valores in vendas_por_mes_dict.items()
            ]
        total_vendas = vendas_total.aggregate(total=Sum("valor"))["total"]   
        print(vendas_por_mes)
        
        context = {
            'antes': Cliente.objects.all(),
            'servicos': Servico.objects.all(),
            'active': active,
            'mes_atual': mes_atual_STR, 
            'vendas_mes_atual': vendas_mes_atual,
            'total_vendas':total_vendas,
            'vendas_mes': vendas_por_mes
        }

    return render(request, "sistema/movimentacao.html", context)

def pedidosView(request):
    
    
    if is_mobile(request):
        mobile = "true"
        carrinhos = Carrinho.objects.all()
        active = "pedidos"

        context = {
            'carrinhos': carrinhos,
            'mobile':mobile,
            'active': active,
        }
        return render(request, "sistema/pedidos.html", context)
    else:
            
        carrinhos = Carrinho.objects.all()
        active = "pedidos"

        context = {
            'carrinhos': carrinhos,
            'active': active,
        }
    return render(request, "sistema/pedidos.html", context)

def carrinhosView(request,id_carrinho):
    
    produtos = Produto_Carrinho.objects.filter(carrinho__id=id_carrinho)
    carrinho = Carrinho.objects.get(id= id_carrinho)
    context = {
         'produto': produtos,
         'carrinho':carrinho
    }
    return render(request, "sistema/carrinho.html", context)


def carrinhoCreateView(request,cliente_nome):
  
    
    try:
        nCarrinho = Carrinho.objects.get(cliente__nome=cliente_nome, data_criado = datetime.datetime.now())
    except:
        
        nCarrinho = Carrinho.objects.all()
        cliente = Cliente.objects.get(nome=cliente_nome, )
    
        nCarrinho.create(
            cliente = cliente,
            total = 0
        ) 
        
    

    context = {
        'clientes': Cliente.objects.all(),
        'servicos': Servico.objects.all(),
        'nome_cliente': cliente_nome
    }

    return render(request, "sistema/addcarrinho.html", context)


def addCarrinnhoView(request):

    if request.method == "POST":
        servico_get = request.POST.get('servico')
        cliente_get = request.POST.get('cliente')
        cliente = Cliente.objects.get(nome=cliente_get)
        servico = Servico.objects.get(nome_servico= servico_get)
        valor=servico.valor
        carrinho = Carrinho.objects.get(cliente=cliente, data_criado = datetime.datetime.now())
        carrinho.total += valor
        carrinho.save()
        
        produto_carrinho = Produto_Carrinho.objects.all()
        produto_carrinho.create(
                carrinho = carrinho,
                servico = servico,
                subtotal= valor           
                
            )
        
        return redirect('pedidos')

    
    return redirect('clientes')



def cadastroCliente(request):
    
    cliente =  Cliente.objects.all()
    if request.method == 'POST':
        
            nome = request.POST.get('nome')
            data_nasc = request.POST.get('data_nascimento')
            telefone = request.POST.get('telefone')
            utlima_entrada = datetime.datetime.now()
            
            cliente.create(
                nome=nome,
                data_nasc=data_nasc,
                telefone=telefone,
                ultima_entrada=utlima_entrada,
            
            )
            return redirect('clientes')
   
    context = {
        'cliente' : cliente,
    }
    print("aqui")
    return render (request , 'sistema\cadastro.html', context)



def clienteView(request,id_cliente):
  
    cliente= Cliente.objects.get(id=id_cliente)

    context = {
        'cliente': cliente,
    }

    return render(request, "sistema/clienteId.html", context)

def clienteEditView(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    
    nome = request.POST.get("nome")
    telefone = request.POST.get("telefone")
    data_nasc = request.POST.get("data_nasc")
    cliente.nome = nome
    cliente.telefone = telefone
    cliente.data_nasc = data_nasc
    print(data_nasc )
    cliente.save()

    return redirect('clientes')



def finalizarView(request, id_carrinho):
    
    
    vendas = Vendas.objects.all()
    carrinho = Carrinho.objects.get(id=id_carrinho)
    produto = Produto_Carrinho.objects.filter(carrinho=carrinho)
    vendas.create(
        data = carrinho.data_criado,
        valor = carrinho.total,
        cliente = carrinho.cliente        
    )    
    carrinho.delete()


    return redirect('vendas')

