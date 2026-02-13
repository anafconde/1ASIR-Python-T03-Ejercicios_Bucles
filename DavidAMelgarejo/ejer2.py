"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo).
El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado), y 
si llegas al límite de intentos, te muestra el número generado.
"""
import random
n=random.randrange(1,101)
intentos=0
while intentos<10:
    try:
        m=int(input("Adivina un numero del 1 y 100"))
        intentos+=1
        if m==n:
            print(f"Enhorabuena era el {n}, lo acertaste en {intentos} intentos")
            break
        elif n<m:
            print(f"El numero es menor que {m}")
        else:
            print(f"El numero es mayor que {m}")
        print(f"Llevas {intentos} intentos, te quedan {10-intentos}")        
    except ValueError:
        print("Error: No es un numero")
else:
    print(f"Mala suerte, numero era {n}")