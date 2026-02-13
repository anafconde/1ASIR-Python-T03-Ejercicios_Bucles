"""
Mostrar en pantalla los N primeros números primos.
Se pide por teclado la cantidad de números primos que queremos mostrar.
"""
import math
while True:
    try:
        n=int(input("Cuantos numeros primos quieres?: "))
        if n>1:break
        else:print("Numero entero mayor que 1")
    except ValueError:
        print("Valor no valido")
num=2
primos=0

while n!=primos:
    esPrimo=True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:esPrimo=False            
        if not esPrimo:break
    else:
        primos+=1
        print(num)
    num+=1
    