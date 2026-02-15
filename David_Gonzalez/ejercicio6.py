# Autor: David González Mora
# versión: 1.0
# Ejercicio 6 Relación de ejercicios
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

n = int(input("Introduce un número: "))
n1 = int(input("Introduce otro número: "))

for i in range(n,n1 +1):
    if i % 2 == 0:
        print(i)
