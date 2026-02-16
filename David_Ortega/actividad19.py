#David Ortega MArfil

print("Que quieres hacer?")
print("1 Sumar")
print("2 Restar")
print("3 Multiplicar")
print("4 Dividir")

opcion = int(input("Elige una opcion"))

if opcion == 1:
    numero1 = int(input("Pon un numero"))
    numero2 = int(input("Pon otro numero"))
    print("La suma es: ", numero1 + numero2)
    
elif opcion == 2:
    numero1 = int(input("Pon un numero"))
    numero2 = int(input("Pon otro numero"))
    print("La resta es: ", numero1 - numero2)
elif opcion == 3:
    numero1 = int(input("Pon un numero"))
    numero2 = int(input("Pon otro numero"))
    print("La multiplicacion es: ", numero1 * numero2)
elif opcion == 4:
    numero1 = int(input("Pon un numero"))
    numero2 = int(input("Pon otro numero"))
    print("La division es: ", numero1 / numero2)
    