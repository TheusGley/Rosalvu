from django.contrib import admin
from django.urls import path, include
# from bond  import urls as bond_urls 
from django.conf.urls.static import static
from django.conf import settings
from .views import *



urlpatterns = [
    path('', homeView, name="home"),
    path('home', homeSystemView, name="index"),
    path('calendario', calendarioView, name="calendario"),
    path('clientes',clientesView, name="clientes"),
    path('clienteEdit/<id_cliente>',clienteEditView, name="clienteEdit"),
    path('cliente/<id_cliente>',clienteView, name="cliente"),
    path('cadastro',cadastroCliente, name="cadastro"),
    path('servicos', servicosView, name="servicos"),
    path('atividades', atividadesView, name="atividades"),
    path('vendas', movimentacaoView, name="vendas"),
    path('pedidos', pedidosView, name="pedidos"),
    path('carrinho/<id_carrinho>', carrinhosView, name="carrinho"),
    path('carrinhoCreate/<cliente_nome>', carrinhoCreateView, name="carrinhoNew"),
    path('addCarrinho', addCarrinnhoView, name="addCarrinho"),
    path('finalizar/<id_carrinho>', finalizarView, name="finalizar"),
    
    
    path('teste/',testeView, name="teste"),
    
    
    
        path('mensagem/', mensagem, name='mensagem'),
    
    
    
    
    
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                            document_root= settings.MEDIA_ROOT)
