# Autor: Felipe
# Version: 1.0
# Ejercicio 2
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio 
# del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es 
# mayor o menor que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
# si se llega al limite de intentos te muestra el número que había generado.

import random

aleatorio= random.randint(1, 100)
numero=int(input("Acierta el numero entre el 1 y el 100: "))
intentos= 10
echos= 0

quedan=intentos - echos


while intentos > echos:
    quedan=intentos - echos
    
    if numero == aleatorio:
        print("Acertastes el numero en ",echos,"intentos")
        break
    elif numero > aleatorio:
        print("Te quedan",quedan,"intentos")
        print("El número secreto es MENOR.")
        echos+=1
        numero=int(input("Acierta el numero entre el 1 y el 100: "))
    else:
        print("Te quedan",quedan,"intentos")
        print("El número secreto es MAYOR.")
        echos+=1
        numero=int(input("Acierta el numero entre el 1 y el 100: "))

if numero != aleatorio:
    print("Ya no te quedan intentos , el numero secreto era:",aleatorio)