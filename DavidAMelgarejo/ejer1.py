"""
Crea una aplicación que pida un número y calcule su factorial.
El factorial de un número es el producto de todos los enteros entre 1 y el 
propio número y se representa por el número seguido de un signo de exclamación.
Por ejemplo: 5! = 1x2x3x4x5 = 120.
"""
import math
while True:
    try:
        n=int(input("Un numero entero positivo: "))
        if n>=0: break
        else: print("No es un entero positivo")
    except ValueError:
        print("Error: Eso no es un numero entero")

print(f"El factorial de {n}! es {math.factorial(n)}")