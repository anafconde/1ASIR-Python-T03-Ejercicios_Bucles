# Autor: Paco Fernandez
# Version: 1.0
# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que 
# seleccionamos la opción de “Salir”.

while True:
    print("--- MENÚ ---")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Salir")
    print("")
    
    opcion = int(input("Elige una opción: "))
    
    match opcion:
        case 1:
            print("Bienvenido")
        case 2:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            resultado = a + b
            print(f"La suma es: {resultado}")
        case 3:
            print("Saliendo del programa...")
            break  
        case _:
            print("Opción no válida, intenta de nuevo.")
