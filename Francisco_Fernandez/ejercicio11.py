# Autor: Paco Fernandez
# Version: 1.0
# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible 
# por algún otro número.

numero = int(input("Introduce un número: "))

contador = 0

for p in range(1, numero + 1): #Recorremos desde el 1 hasta el numero introducido, cada vez que el dividor
    if numero % p == 0:        #sea 0 sumamos uno al contador, si es primo  tendra contador=2..
        contador += 1

if contador == 2:
    print("Es primo")
else:
    print("No es primo")
