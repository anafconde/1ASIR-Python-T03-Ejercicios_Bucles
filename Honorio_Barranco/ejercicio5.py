# Autor: Honorio
# Version: 1.0
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario.
#El programa termina cuando se introduce un espacio.
import os
os.system("cls")
carac=input("Introduzca una vocal (ESPACIO para salir): ")
while carac != " ":
    if carac == "a" or carac == "e" or carac == "i" or carac == "o" or carac == "u":
        print("VOCAL MINUSCULA")
    elif carac == "A" or carac == "E" or carac == "I" or carac == "O" or carac == "U":
        print("VOCAL MAYUSCULA")
    else:
        print("NO VOCAL")
    carac=input("Introduzca una vocal (ESPACIO para salir): ")
print ("FIN DEL PROGRAMA")