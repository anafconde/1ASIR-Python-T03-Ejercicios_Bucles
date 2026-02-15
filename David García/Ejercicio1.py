# Author: David García Pérez
# Version: 1.0

# Ejercicio 1
# Crea una aplicación que pida un número y calcule su factorial
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número
# y se representa por el número seguido de un signo de exclamación.
# Por ejemplo 5! = 1x2x3x4x5=120).

import os
os.system("cls")

print(" ")
print("#################### Calcular factorial de un número ######################")
print(" ")

num = int(input("Introduce un número: "))

factorial = 1
cont = 1

while cont <= num:
    factorial = factorial * cont
    cont = cont + 1

print(f"El factorial de {num} es {factorial}")

print(" ")
print("#################### Fin del programa ######################")
print(" ")