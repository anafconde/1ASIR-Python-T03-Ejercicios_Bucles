# Author: David García Pérez
# Version: 1.0

# Ejercicio 11
# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import os
os.system("cls")

import math

print(" ")
print("#################### Comprobar números primos ######################")
print(" ")

num = int(input("Introduce un número: "))

if num <= 1:
    print(f"El número {num} no es primo")
else:
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            print(f"El número {num} no es primo")
            break
    else:
        print(f"El número {num} es primo")

print(" ")
print("#################### Fin del programa ######################")
print(" ")