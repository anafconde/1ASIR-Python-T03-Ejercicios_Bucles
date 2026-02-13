# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 8: Intervalo de números.
# Escribe un programa que pida el límite inferior y superior de un intervalo.
# Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
# A continuación, se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa, dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuántos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.


# Pedimos los límites
limite_inferior = int(input("Introduce el límite inferior: "))
limite_superior = int(input("Introduce el límite superior: "))

while limite_inferior > limite_superior:
    print("El límite inferior no puede ser mayor que el superior.")
    limite_inferior = int(input("Introduce el límite inferior: "))
    limite_superior = int(input("Introduce el límite superior: "))

suma = 0
fuera = 0
iguales = 0   

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    
    if numero > limite_inferior and numero < limite_superior:
        suma = suma + numero
    
    elif numero < limite_inferior or numero > limite_superior:
        fuera = fuera + 1
    
    if numero == limite_inferior or numero == limite_superior:
        iguales = iguales + 1
    
    numero = int(input("Introduce un número (0 para terminar): "))

print("Suma dentro del intervalo:", suma)
print("Cantidad fuera del intervalo:", fuera)

if iguales > 0:
    print("Se ha introducido algún número igual a los límites.")
else:
    print("No se ha introducido ningún número igual a los límites.")


