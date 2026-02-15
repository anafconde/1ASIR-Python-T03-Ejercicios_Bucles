"""
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.
"""
from datetime import date
import os,sys
while True:
    print("\t Menu")
    print("a)Fecha actual\nb)Saluda\nc)Limpia consola\nd)Salir\nSeleccione una opcion:")
    option=input("").lower().strip()
    if option=="a":
        print(f"Fecha actual: {date.today()}")
    elif option=="b":
        print(f"Hola {os.getlogin()}")
    elif option=="c":
        os.system("clear")
    elif option=="d":
        print("Saliendo del programa...")
        sys.exit()
    else:print("Opcion no valida")
 
        