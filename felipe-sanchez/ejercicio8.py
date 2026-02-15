# Autor: Felipe
# Version: 1.0
# Ejercicio 8
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

# •         La suma de los números que están dentro del intervalo (intervalo abierto).

# •         Cuantos números están fuera del intervalo.

# •         He informa si hemos introducido algún número igual a los límites del intervalo.



inferior=int(input("Dame un numero para limite inferior: "))
superior=int(input("Dame un numero para limite superior: "))

dentro=0
fuera=0
igual=0


while inferior > superior:
    print("Datos introducidos erroneos, vuelva a introducirlos:")
    inferior=int(input("Dame un numero para limite inferior: "))
    superior=int(input("Dame un numero para limite superior: "))

while True:
    print("Comienza a introducir numeros, introduzca 0 para salir")
    
    numero=int(input("Introduzca el numero: "))
    
    if numero == 0:
        break
    
    if superior > numero > inferior:
        dentro+=numero
    elif numero > superior or numero < inferior:
        fuera+=1
    elif numero == inferior:
        print("El numero introducido es igual al numero del dato inferior")
    elif numero == superior:
        print("El numero introducido es igual al numero del dato superior")

        
print("Cantidad de numero fuera del rango: ",fuera)
print("Cantidad de numero dentro del rango: ",dentro)