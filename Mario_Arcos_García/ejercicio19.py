# autor: Mario Arcos
# version: 1.0
# ejercicio 19

opcion = 0

while opcion != 3:
    print("1. Saludar 2. Piedra, papel o tijera 3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("¡Hola!")
    elif opcion == 2:
        print("¡Ganaste!")
    elif opcion == 3:
        print("Adiós")
    else:
        print("Opción incorrecta")