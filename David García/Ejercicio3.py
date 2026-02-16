# Author: David García Pérez
# Version: 1.0

# Ejercicio 3
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

import os
os.system("cls")

print(" ")
print("#################### Suma y media de números ######################")
print(" ")

num = int(input("Introduce un número: "))
suma = 0
cont = 0

if num == 0:
    exit
else:
    while num != 0:
        cont = cont + 1
        suma = suma + num
        num = int(input("Introduce otro número: "))
        media = suma / cont
    print(f"La suma de los números introducidos es {suma} y la media es {media}")

print(" ")
print("#################### Fin del programa ######################")
print(" ")