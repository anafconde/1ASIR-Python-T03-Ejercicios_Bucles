# Autor: Paco Fernandez
# Version: 1.0
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, 
# el programa termina cuando se introduce un espacio.

caracter = ""
while caracter != " ":
    caracter = input("Introduce un caracter (espacio para salir): ")

    if caracter == " ":     
        print("Saliendo")
        break

    if caracter.upper() == "A" or caracter.upper() == "E" or caracter.upper() == "I" or caracter.upper() == "O" or caracter.upper() == "U":
        print("VOCAL")
    else:
        print("NO VOCAL")