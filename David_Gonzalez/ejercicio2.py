# Autor: David González Mora
# versión: 1.0
# Ejercicio 2 Relación de ejercicios
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

numero = random.randint(1,100)

intentos = 0

print("Adivina el número (1-100)")

while intentos < 10:
    n = int(input("Introduce un número: "))
    intentos += 1
    
    if n == numero:
        print("Número Acertado")
        break
    elif n < numero:
        print("El número es mayor ", "Los intentos restantes són",10-intentos)
    else:
        print("El número es menor","Los intentos restantes són",10-intentos)
    

print("Se acabaron los intentos", "El número es", numero)
