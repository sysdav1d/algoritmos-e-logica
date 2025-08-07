"""
Problema "idades"
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. 
"""

def media_idade(idade1,idade2):
    return ((idade1) + (idade2)) / 2


print("Dados da primeira pessoa: ")
primeira_pessoa_nome = input("Digite o Nome: ")
primeira_pessoa_idade = float(input("Digite a idade: "))

print("Dados da segunda pessoa: ")
segunda_pessoa_nome = input("Digite o Nome: ")
segunda_pessoa_idade = float(input("Digite a idade: "))

print(f"A idade média de {primeira_pessoa_nome} e {segunda_pessoa_nome} é de {media_idade(primeira_pessoa_idade,segunda_pessoa_idade):.2f} anos")
