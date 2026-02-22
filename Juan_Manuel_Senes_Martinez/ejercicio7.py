#Realice un algoritmo que muestre la tabla de multiplicar de un número introducido por el teclado.
import os
os
numero=int(input("introduce un numerro para dar la tabla de multiplicar")) 
print ("la tabla de", numero, "es")
for n in range(1,11):
    res= numero * n

    print (numero, " X ",n , "=", res,)