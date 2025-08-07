nome_funcionario = input("Nome: ")
valor_por_hora = float(input("Valor por hora: "))
horas_trabalhadas = float(input("Horas trabalhadas: "))

pagamento = valor_por_hora * horas_trabalhadas

print(f"o pagamento para {nome_funcionario} deve ser {pagamento:.2f}")
