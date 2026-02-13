# Autor: Honorio
# Version: 1.0
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número 
# es el producto de todos los enteros entre 1 y el propio número y se representa por el número 
# seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).
import os
os.system("cls")
import math
num=int(input("Introduzca un numero: "))
fac=1

while fac <= num:
    fac = fac +1
    facturial=math.factorial(num)
print(f" El facturial de {num} = {facturial}")

    
