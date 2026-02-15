# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 6
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

for n in range(numero1,numero2 + 1):
    if n % 2 == 0 :
        print(f"Numeros pares: {n}")

        