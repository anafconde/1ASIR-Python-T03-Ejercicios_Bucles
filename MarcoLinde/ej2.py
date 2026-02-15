#Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación genera un 
#número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo 
#si el número a adivinar es mayor o menor que el introducido, a demás de los intentos 
#que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando 
#se acierta el número (además te dice en cuantos intentos lo has acertado), si se 
#llega al limite de intentos te muestra el número que había generado.
import random
num= random.randint(1, 100)
intent= 10
bien= False
while intent>0 and not bien:
    print("Te quedan", intent, "intentos")
    pernum= float(input("Pon un número del 1 al 100: "))
    if pernum==num:
        bien= True
    else:
        if num>pernum:
            print("El número es mayor que: ", pernum)
        else:
            print("El número es menor que: ", pernum)
        intent= intent-1
if bien:
    print("Has acertado, el número es: ", num)
    print("Lo has conseguido en", 10-intent, "intentos")
else:
    print("Has llegado al límite de intentos, el número es: ", num)
