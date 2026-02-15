# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 8
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el 
# superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:
# •         La suma de los números que están dentro del intervalo (intervalo abierto).
# •         Cuantos números están fuera del intervalo.
# •         He informa si hemos introducido algún número igual a los límites del intervalo.

limit_infe = int(input("Introduce un limite inferior: "))
limit_supe = int(input("Introduce un limite superior: "))

while limit_infe > limit_supe:
    print("Error: El límite inferior no puede ser mayor que el superior.")
    limit_infe = int(input("Introduce un limite inferior: "))
    limit_supe = int(input("Introduce un limite superior: "))

suma = 0
fuera = 0
igual = 0 

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:

    if numero > limit_infe and numero < limit_supe:
        suma = suma + numero
    else:
        fuera = fuera + 1

    if numero == limit_infe or numero == limit_supe:
        igual = igual + 1

    numero = int(input("Introduce un número (0 para terminar): "))

print("Suma de los números dentro del intervalo:", suma)
print("Cantidad de números fuera del intervalo:", fuera)

if igual > 0:
    print("Se ha introducido algún número igual a los límites.")
else:
    print("No se ha introducido ningún número igual a los límites.")
