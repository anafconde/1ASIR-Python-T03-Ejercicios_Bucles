import random

secreto = random.randint(1, 100)
intentos_restantes = 10
acertado = False

while intentos_restantes > 0 and acertado == False:
    print("Intentos restantes:", intentos_restantes)
    numero = int(input("Dime un número (1-100): "))
    
    if numero == secreto:
        print("¡Acertaste! Lo has logrado en", 11 - intentos_restantes, "intentos.")
        acertado = True
    elif numero < secreto:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
    
    intentos_restantes -= 1

if acertado == False:
    print("Te has quedado sin intentos. El número era:", secreto)