from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRASACOES = []

def Cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    LISTA_CATEGORIAS.append(nova_categoria)
    return nova_categoria

def Cadasrtrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(descricao=descricao, valor=valor, categoria=categoria)
    LISTA_TRASACOES.append(nova_transacao)
    return nova_transacao

def Saldo_total():
    total = 0
    for t in LISTA_TRASACOES:
        total += + t.valor
    return total
