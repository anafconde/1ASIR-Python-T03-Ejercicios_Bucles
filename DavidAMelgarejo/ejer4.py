"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""
while True:
    try:
        n=int(input("Cuantos numeros va a introducir?: "))
        if n>=0: break
        else: print("No es un entero positivo")
    except ValueError:
        print("Error: Eso no es un numero entero")
positivos=negativos=ceros=0
while n>0:
    try:
        m=int(input("Numero: "))
        if m>0:
            positivos+=1
        elif m<0:
            negativos+=1
        else:
            ceros+=1
        n-=1
    except ValueError:
        print("Numero no válido")
print(f"Hay {positivos} positivos, {negativos} negativos y {ceros} ceros")