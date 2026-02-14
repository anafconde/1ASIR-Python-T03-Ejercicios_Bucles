# Author: David García Pérez
# Version: 1.0

# Ejercicio 19
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

import os
os.system("cls")

print(" ")
print("#################### Calculadora ######################")
print(" ")

opc = 0

while opc != 5:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opc = int(input("Elige una opción: "))

    if opc == 1:
        num1 = float(input("Introduce primer número: "))
        num2 = float(input("Introduce segundo número: "))
        suma = num1 + num2
        print(f"La suma de {num1} + {num2} es: {suma}")
    elif opc == 2:
        num1 = float(input("Introduce primer número: "))
        num2 = float(input("Introduce segundo número: "))
        resta = num1 - num2
        print(f"La resta de {num1} - {num2} es: {resta}")
    elif opc == 3:
        num1 = float(input("Introduce primer número: "))
        num2 = float(input("Introduce segundo número: "))
        producto = num1 * num2
        print(f"El producto de {num1} * {num2} es: {producto}")
    elif opc == 4:
        num1 = float(input("Introduce primer número: "))
        num2 = float(input("Introduce segundo número: "))
        if num2 != 0:
            division = num1 / num2
            print(f"La división de {num1} / {num2} es: {division}")
        else:
            print("No se puede dividir entre 0")
    elif opc == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Inténtalo de nuevo")

print(" ")
print("#################### Fin del programa ######################")
print(" ")