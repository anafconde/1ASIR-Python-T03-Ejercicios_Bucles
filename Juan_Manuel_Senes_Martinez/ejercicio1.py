#Crea una aplicación que pide un número y calcula su factorial . El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación.

import math

numero=[]
numero = int(input("indica un numero y te doy su factorial"))

factorial=(math.factorial(numero))

print("el factorial de:", numero, "es",factorial)