#Ejercicio 8
#Escribe un programa que pida el limite inferior y superior de un intervalo. 
#Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
#A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando 
#termine el programa dará las siguientes informaciones:
#• La suma de los números que están dentro del intervalo (intervalo abierto).
#• Cuantos números están fuera del intervalo.
#• He informa si hemos introducido algún número igual a los límites del intervalo.
liminf= int(input("Límite inferior: "))
limsup= int(input("Límite superior: "))
while liminf>limsup:
    print("El límite inferior es mayor que el superior, vuelve a poner tus parámetros: ")
    liminf = int(input("Límite inferior: "))
    limsup = int(input("Límite superior: "))
suma= 0
fuera= 0
limigual= False
num= int(input("Pon un número (0 para parar): "))
while num!= 0:
    if num==liminf or num==limsup:
        limigual= True
    if num>liminf and num<limsup:
        suma= suma+num
    else:
        if num!= 0:
            fuera= fuera+1
    num= int(input("Pon otro número (0 para parar): "))
print("La suma de los números dentro del intervalo es: ", suma)
print("Los números fuera del intervalo son: ", fuera)
if limigual:
    print("Se han puesto números igual/es a los límites")
else:
    print("No se han puesto números igual/es a los límites")
