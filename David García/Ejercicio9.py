# Author: David García Pérez
# Version: 1.0

# Ejercicio 9
# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
# No se puede utilizar el operador de potencia.

import os
os.system("cls")

print(" ")
print("#################### Calcular potencias ######################")
print(" ")

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

potencia = 1

for e in range(exponente):
    potencia = potencia * base

print(f"La potencia de {base} elevado a {exponente} es: {potencia}")

print(" ")
print("#################### Fin del programa ######################")
print(" ")