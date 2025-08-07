"""
Problema "consumo"
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais. 

"""

distacia_pecorrida = int(input("Distancia percorrida: "))
combustivel_gasto = float(input("Combustivel gasto: "))

consumo_medio = (distacia_pecorrida / combustivel_gasto)

print(f"Consumo medio = {consumo_medio:.3f}")
