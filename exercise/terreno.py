"""
Problema "terreno"
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais, conforme exemplo. 
"""

largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite a largura do terreno: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrao: "))

area_do_terreno = largura_terreno * comprimento_terreno
preco_do_terreno = area_do_terreno * valor_metro_quadrado


print(f"Area do terreno = {area_do_terreno:.2f}")
print(f"Preco do terreno = {preco_do_terreno:.2f}")