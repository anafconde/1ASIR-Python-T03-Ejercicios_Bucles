#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.  
#A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# además de los intentos que te quedan (tienes 10 intentos para acertarlo).  
#El programa termina cuando se acierta el número (además te dice en cuántos intentos lo has acertado), 
# y si llegas al límite de intentos, te muestra el número generado.

import random
rdm = random.randint(1,100)
num = 0
contador = 0
print (rdm)

while rdm != num and contador != 10:
    print ("-------------ADIVINANDO-------------")
    num = int(input("Dime el número a adivinar (1,100): "))
    if num > rdm:
        print ("El número a adivinar es menor.")
    elif num < rdm: 
        print ("El número a adivinar es mayor.")
    elif num == rdm:
        print ("Enhorabuena has adivinado el número.")
    contador = contador + 1




