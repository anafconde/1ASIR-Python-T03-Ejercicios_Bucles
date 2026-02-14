"""
Escribe un programa que diga si un número introducido por teclado es o no primo.
Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
"""
import math
while True:
    try:
        n=int(input("Numero: "))
        if n>1:break
        else:print("Tiene que ser entero mayor que 1")
    except ValueError:
        print("No es un numero")
cont=0
esPrimo=True
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:esPrimo=False
    if not esPrimo:
        print("No es primo")
        break
else:
    print("Es primo")