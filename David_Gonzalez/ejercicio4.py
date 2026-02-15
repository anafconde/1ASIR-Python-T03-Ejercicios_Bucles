# Autor: David González Mora
# versión: 1.0
# Ejercicio 4 Relación de ejercicios
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input("Introduce la cantidad de números que quieres introducir: "))

contar = 0

mayor = 0
menor = 0
igual = 0

while contar < cantidad:
    n = int(input("Introduce un número: "))
    contar += 1
    if n < 0:
        menor += 1
    elif n > 0:
        mayor += 1
    else:
        igual += 1

print("Números introducidos mayores que 0: ", mayor)
print("Números introducidos menores que 0: ", menor)
print("Números introducidos igual a 0: ", igual)
