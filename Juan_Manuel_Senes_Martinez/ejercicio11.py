#Escribe un programa que diga si un número introducido por teclado es o no primo .
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
#Nota : Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.


import math 
numero=int(input("introduce un numero"))

for n in range(2,int(math.sqrt(numero)+1)):

    resultado=(numero%n)

if resultado==0:
    print(numero,"no es primo")
else:
    print(numero,"es primo")
    
