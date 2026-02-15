# Autor: Honorio
# Version: 1.0
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
import os
os.system("cls")

numero=int(input("Introduzca un numero: "))
sumar= 0
cont= 0
if numero == 0:
    exit
    print("Fin del programa")
else:
    while numero != 0:
        cont= cont + 1
        sumar=sumar + numero
        numero=int(input("Introduzca un numero: "))
        media = sumar / cont
    print(f"La suma es {sumar} y la media {media}")
print("Fin del programa")
