"""
Problema "retangulo"
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
"""

import math

base_retangulo = float(input("Digite base do retangulo"))
altura_retangulo = float(input("Digite altura do retangulo"))

def area_retangulo(b,h):
    return b * h

def perimetro_retangulo(b,h):
    return 2 * (b + h)

def diagonal_retangulo(b, h):
    return math.sqrt(pow(b,2) + pow(h,2))

perimetro = perimetro_retangulo(base_retangulo,altura_retangulo)
area = area_retangulo(base_retangulo,altura_retangulo)
diagonal = diagonal_retangulo(base_retangulo,altura_retangulo)


print(f"AREA: {area:.4f} ")
print(f"perimetro: {perimetro:.4f} ")
print(f"Diagonal: {diagonal:.4f}")