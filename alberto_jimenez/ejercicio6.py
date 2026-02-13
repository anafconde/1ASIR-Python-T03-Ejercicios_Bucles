#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

ini = int(input("Dime un número inicial: "))
fin = int(input("Dime un número final: "))

cont = 0
print ("---------------PAR O IMPAR---------------")
while cont != fin:
    
    if cont % 2 == 0:
        print (f"El número {cont} es par")
    else:
        print (f"El número {cont} no es par")
    cont = cont + 1





