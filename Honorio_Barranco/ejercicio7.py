# Autor: Honorio
# Version: 1.0
#Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
import os
os.system("cls")

num=int(input("Introduzca el numero que quieres multiplicar: "))

for n in range(0,11):
    multiplicar=num*n
    print(f"{num} x {n} = {multiplicar}")
print("Fin del programa")