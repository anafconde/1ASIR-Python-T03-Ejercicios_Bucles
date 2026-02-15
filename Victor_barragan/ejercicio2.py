# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 2
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número 
# (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

num= random.randint(1, 100)
intentos = 10
ganaste = False

print("Adivina el numero de la maquina aleatorio")
print(f"Tienes {intentos} intentos para adivinar un número entre 1 y 100.")

for i in range(1,intentos +1):
    n1=int(input("Dame un numero del 1-100 para jugar con los aleatorios: "))

    if n1 == num:
        print(f"¡Exacto! Lo has logrado en {i} intentos.")
        ganaste = True
        break # Salimos del bucle porque ya acertó
    elif n1 > num:
       print("El número a adivinar es MENOR.")
    else:
        print("El número a adivinar es MAYOR.")
    
    # Informamos cuántos intentos quedan
    if i < intentos:
        print(f"Te quedan {intentos - i} intentos.")

# Si terminan los intentos y no acertó
if not ganaste:
    print(f"\Lo siento, te has quedado sin intentos. El número era el {num}.")
          
