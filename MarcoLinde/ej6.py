#Ejercicio 6
#Escribir un programa que imprima todos los números pares entre dos 
#números que se le pidan al usuario.
prin= int(input("Pon un número: "))
fin= int(input("Pon otro número: "))
print("Números pares entre estos números: ")
for n in range(prin, fin +1):
    if n %2==0:
        print(n)
