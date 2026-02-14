"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario.
El programa termina cuando se introduce un espacio.
"""
while True:
    letra=input("Introduzca un caracter (espacio para salir): ").lower()
    if letra in ["a","e","i","o","u"]:
        print("VOCAL")
    elif letra==" ":break
    else:
        print("NO VOCAL")