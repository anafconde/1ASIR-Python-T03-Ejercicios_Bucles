# Author: David García Pérez
# Version: 1.0

# Ejercicio 5
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
# el programa termina cuando se introduce un espacio.

import os
os.system("cls")

print(" ")
print("#################### Comprobar si los caracteres son vocal o no vocal ######################")
print(" ")

while True:
    caracter = input("Introduce un carácter (espacio para salir): ")
    if caracter == " ":
        break
    
    if caracter.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")

print(" ")
print("#################### Fin del programa ######################")
print(" ")