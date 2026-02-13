"""
Escribe un programa que pida el límite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
A continuación, se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa, dará las siguientes informaciones:

    La suma de los números que están dentro del intervalo (intervalo abierto).
    Cuántos números están fuera del intervalo.
    Informa si hemos introducido algún número igual a los límites del intervalo.

"""
while True:
    try:
        supe=int(input("Limite superior: "))
        infe=int(input("Limite inferior: "))
        if infe<supe:break
        else: print("El inferior no puede ser mayor o igual que el superior")
    except ValueError:
        print("Error: No es un numero entero")
suma=iguales=out=0
while True:
    try:
        num=int(input("Escribe un numero(0 para terminar): "))
        if num==0:break
        elif num>infe and num<supe:
            suma+=num
        elif num==infe or num==supe:
            iguales+=1
        else:
            out+=1
    except ValueError:
        print("Error: No es un numero entero")
print(f"La suma de los numeros del intervalo es: {suma} \n Hay {iguales} numeros iguales que los limites {infe} y {supe} \n Y {out} numeros fuera del intervalo")