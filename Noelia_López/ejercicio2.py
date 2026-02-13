# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-13

# Ejercicio 2: Adivina el número. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
# A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# además de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado), 
# y si llegas al límite de intentos, te muestra el número generado.

import random

secreto = random.randint(1,100)
intentos = 10 
print("Tienes 10 intentos para adivinar el número secreto entre 1 y 100.")
while intentos > 0:
    adivina = int(input("Introduce tu intento: "))
    if adivina == secreto:
        print(f"Has acertado el número en {11 - intentos} intentos.")
        break
    elif adivina < secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intentos -= 1
else:
    print(f"Has agotado tus intentos. El número era {secreto}.")