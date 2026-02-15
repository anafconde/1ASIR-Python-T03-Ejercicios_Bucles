# Autor: Honorio
# Version: 1.0
#Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
#No se puede utilizar el operador de potencia.
import os 
os.system("cls")

numbase=int(input("Introduzca el numero base: "))
numexpon=int(input("Introduzca el numero exponente (positivo): "))
resultado=1
if numexpon < 0:
    print("El exponente tiene que ser positivo")
else:
    for n in range(numexpon):
        resultado = resultado * numbase
    print(f"El resultado de la base {numbase} y el exponente {numexpon} es {resultado}")
print("FIN DEL PROGRAMA")
