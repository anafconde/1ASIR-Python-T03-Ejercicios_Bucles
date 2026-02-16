# autor: Mario Arcos
# version: 1.0
# ejercicio 9

base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

resultado = 1

for i in range(exponente):
    resultado = resultado * base

print("El resultado es:", resultado)