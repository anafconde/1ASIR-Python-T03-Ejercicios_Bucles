# Autor : Miguel Vilchez
# Version : "1.0"

import random
numero_secreto = random.randint(1, 100)
intentos_restantes = 10
acertado = False

print("He pensado un número del 1 al 100. Tienes 10 intentos.")
while intentos_restantes > 0 and not acertado:
    print(f"Te quedan {intentos_restantes} intentos.")
    intento = int(input("Introduce tu número: "))
    
    if intento == numero_secreto:
        acertado = True
        print(f"¡Exacto! Lo has logrado en {11 - intentos_restantes} intentos.")
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    intentos_restantes -= 1

if not acertado:
    print(f"Se agotaron los intentos. El número era {numero_secreto}.")