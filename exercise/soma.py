"""
Problema "soma"
Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
números. 

"""

def soma(x,y):
    return x + y

x = int(input("Digite o valor de X:"))
y = int(input("Digite o valor de Y:"))

soma = soma(x,y)
print(F"SOMA = {soma}")
