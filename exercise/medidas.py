a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

area_do_quadrado = a * a
area_do_triangulo = (a * b) / 2
area_do_trapezio = (a + b) * c /2

print(f"AREA DO QUADRADO = {area_do_quadrado:.4f}")
print(f"AREA DO TRIANGULO = {area_do_triangulo:.4f}")
print(f"AREA DO TRAPEZIO = {area_do_trapezio:.4f}")