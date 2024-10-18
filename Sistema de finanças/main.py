from utilitarios import (Cadastrar_categoria, Cadasrtrar_transacao, Saldo_total)

#CATEGORIAS
cadastrar_receitas = Cadastrar_categoria("Receitas")
cadastrar_contas = Cadastrar_categoria("Contas Fixas")
cadastrar_viagens = Cadastrar_categoria("Viagens")

#TRANSAÇÕES
Cadasrtrar_transacao(descricao= "Salário Jan/2024", valor= 1300.0, categoria= cadastrar_receitas)
Cadasrtrar_transacao(descricao= "Mesada mamês", valor= 70.0, categoria=cadastrar_receitas)
Cadasrtrar_transacao(descricao= "Viagem á Mato Grosso do Sul", valor= -50.0, categoria=cadastrar_viagens)
Cadasrtrar_transacao(descricao= "Conta de Internet", valor= -150.0, categoria=cadastrar_contas)

total = Saldo_total()

print(f"Saldo total = {total}")