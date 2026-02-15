# Autor: David González Mora
# versión: 1.0
# Ejercicio 8 Relación de ejercicios
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuantos números están fuera del intervalo.
#He informa si hemos introducido algún número igual a los límites del intervalo.

li = int(input("Límite inferior: "))
ls = int(input("Límite superior: "))

while li > ls:
    print("Error. El inferior no puede ser mayor.")
    li = int(input("Límite inferior: "))
    ls = int(input("Límite superior: "))

suma = 0
fuera = 0
igual = False

num = int(input("Número (0 para terminar): "))

while num != 0:
    
    if num > li and num < ls:
        suma = suma + num
    else:
        fuera = fuera + 1
    
    if num == li or num == ls:
        igual = True
    
    num = int(input("Número (0 para terminar): "))

print("Suma dentro:", suma)
print("Fuera:", fuera)

if igual:
    print("Se introdujo un número igual a un límite.")
else:
    print("No se introdujo ningún número igual a los límites.")
