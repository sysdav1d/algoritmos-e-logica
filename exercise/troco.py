"""
Problema "troco"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente. 

"""

def calcular_troco(preco_unitario,qtd_comprada,dinheiro_recebido):
    total_produto = preco_unitario * qtd_comprada
    return dinheiro_recebido - total_produto

preco_unitario = float(input("Preço unitário do produto: "))
qtd_comprada = float(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

troco_final = calcular_troco(preco_unitario,qtd_comprada,dinheiro_recebido)
print(f"Troco = {troco_final:.2f}")