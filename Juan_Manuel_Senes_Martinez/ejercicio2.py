#Algoritmo que pide números hasta que se introduce un cero .
#Debe imprimir la suma y la media de todos los números introducidos.

import os

numero=[]
while True: 
    n=int(input("indica un numero: "))
    if n == 0:
        break
    numero.append(n)
    print("la suma es",sum(numero))
    print ("la media es ",sum(numero)/len(numero))