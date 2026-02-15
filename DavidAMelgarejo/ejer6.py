"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
"""
n=m=0
while True:
    try:
        n=int(input("Numero 1: "))
        m=int(input("Numero 2: "))
        if n>m:
            m,n=n,m
        break
    except ValueError:
        print("No es un numero entero")
if n%2!=0:
    n+=1
for i in range(n,m+1,2):
    print(i)