#Autor: Alberto Jiménez Mellado
#Version: 1.0
#Escribe un programa que pida el límite inferior y superior de un intervalo.
#Si el límite inferior es mayor que el superior, lo tiene que volver a pedir.
#A continuación, se van introduciendo números hasta que introduzcamos el 0.
#Cuando termine el programa, dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuántos números están fuera del intervalo.
#Informa si hemos introducido algún número igual a los límites del intervalo.

sum = 0
out = 0
num = 1

limin = int(input("Defina el límite inferior: "))
limsup= int(input("Defina el límite superior: "))

while limin > limsup:
    print ("Error. El límite inferior no puede ser más grande al superior.")
    limin = int(input("Defina el límite inferior: "))
    limsup= int(input("Defina el límite superior: "))

while num != 0:
    num = int(input("Dime números (0 para salir): "))
    if num > limin and num < limsup:
        sum += num
    elif num < limin or num > limsup:
        out =+ 1

print (f"La suma total de los números es {sum}.")
print (f"El número de veces que has salido del rango {limin} y {limsup} es {out}.")






