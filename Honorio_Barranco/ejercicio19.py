# Autor: Honorio
# Version: 1.0
#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.
import os
os.system("cls")
menu=0

while menu != "3":
    print("---Menu---")
    print("1.Saludar")
    print("2.Suma de dos numeros")
    print("3.Salir")
    menu=int(input("Eliga la opcion (1-3): "))

    if menu == 1:
        nombre=input("Dime tu nombre: ")
        print(f"Hola {nombre}")
    elif menu == 2:
        num1=int(input("Introduzca el numero1: "))
        num2=int(input("Introduzca el numero2: "))
        suma=num1 + num2
        print(f"{num1} + {num2} = {suma}")
    elif menu == 3:
        print("Adios saliste del menu")
        break
    else:
        print("ERROR la opcion que has introducido no es correcta")

