# Autor: Felipe
# Version: 1.0
# Ejercicio 6
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

nume1=int(input("Dame un numero: "))
nume2=int(input("Dame otro numero: "))


if nume1 < nume2:
    for n in range(nume1,nume2 +1):
        if n %2 == 0:
            print(n)
else:
    for n in range(nume2 ,nume1 +1):
        if n %2 == 0:
            print(n)