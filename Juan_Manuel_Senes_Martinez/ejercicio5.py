#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario.
#El programa termina cuando se introduce un espacio .

vocales = ["A","E","I","O","U"]

while True: 
    letra=input("introduce letras")
    if letra in vocales:
        print("VOCAL")
    else:
        print("no vocal")
        break
