#David Ortega MArfil

numero = int(input("Pon un numero"))
contador = 0

while numero != 0:
    suma = numero + suma
    contador = contador + 1
    numero = int(input("Pon un numero"))
    
if numero == 0:
    print("La suma es: ", suma)
    print("La media es: ", suma / contador)