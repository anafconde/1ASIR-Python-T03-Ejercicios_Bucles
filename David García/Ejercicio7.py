# Author: David García Pérez
# Version: 1.0

# Ejercicio 7
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

import os
os.system("cls")

print()
print("#################### Tablas de multiplicar ######################")
print()

num = int(input("Introduce un número: "))

for n in range(11):
    print(num, "x", n, "=", num * n)

print()
print("#################### Fin del programa ######################")
print()