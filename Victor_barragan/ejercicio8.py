# Autor : Victor Manuel
# Version : "1.0"
# Ejercicio 8:
# Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo. 

num = int(input("Limite inferior: "))
num1 = int(input("Limite superior: "))

while num > num1 :
    num = int(input("Limite inferior: "))
    num1 = int(input("Limite superior: "))
    
suma = 0
fuera = 0
igual = False
num3 = 1

while num3 != 0:
    num3 = int(input("Introduce un numero y para salir un 0: "))
    
    if num3 != 0:
        # ¿Está en medio?
        if num3 > num and num3 < num1:
            suma = suma + num3
        # ¿Es igual a los bordes?
        elif num3 == num or num3 == num1:
            igual = True
        # Si no, está fuera
        else:
            fuera = fuera + 1
    
# 2. Mostramos los resultados
print("Suma de los de dentro:", suma)
print("Cuántos fuera:", fuera)

if igual == True:
    print("Sí, pusiste algún número igual a los límites.")
else:
    print("No pusiste ningún número igual a los límites.")