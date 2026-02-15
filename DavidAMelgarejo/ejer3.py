"""
Algoritmo que pida números hasta que se introduzca un cero.
Debe imprimir la suma y la media de todos los números introducidos.
"""
numeros=[]
while True:
    try:
        n=float(input("Introduce un numero (0 para parar): "))
        if n==0: break
        numeros.append(n)
    except ValueError:
        print("Error: Eso no es un numero")
if numeros:
    suma=sum(numeros)
    print(f"La suma total es:{suma} \n La media es: {suma/len(numeros)}")
else:
    print("No introdujo ningún numero")