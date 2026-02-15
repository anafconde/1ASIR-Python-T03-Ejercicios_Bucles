#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).  
#El programa debe informar de cuántos números introducidos son **mayores que 0**, **menores que 0** e **iguales a 0**.

num = 0

while num != 1:
    print ("-----------VALORANDO NÚMEROS-------------")
    num = int(input("Dime un número ('1' para salir): "))
    if num == 0:
        print (f"El número {num} es igual a 0")
    elif num > 0:
        print (f"El número {num} es mayor a 0")
    elif num < 0: 
        print (f"El número {num} es menor a 0")
    else:
        print ("Debes de indicar un número.")