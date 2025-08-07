def hora_completa(segundos):
    horas = segundos // 3600
    minuto = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return f"{horas:02}:{minuto:02}:{segundos_restantes:02}"

segundos = int(input("Digite os segundos"))

print(hora_completa(segundos))
