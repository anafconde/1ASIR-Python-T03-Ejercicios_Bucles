# Autor: Honorio
# Version: 1.0
#Escribe un programa que diga si un número introducido por teclado es o no primo.
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
#Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
import os
os.system("cls")
primos=int(input("Introduzca un numero: "))
esprimo=1
for n in range(2,primos):
    if primos % n == 0:
        esprimo=0
        break
if esprimo == 1:
    print("Es primo")
else:
    print("No es primo")