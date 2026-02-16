# Autor: Paco Fernandez
# Version: 1.0
# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número 
# y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

numero=int(input("Introduce un numero para calcular el factorial: "))

if numero < 0:
    print("No se puede calcular el factorial de numeros negativos. ")
else:
    factorial=1
    for p in range(1, numero + 1):
        factorial*= p

    print(f"El factorial de {numero} es {factorial}")

