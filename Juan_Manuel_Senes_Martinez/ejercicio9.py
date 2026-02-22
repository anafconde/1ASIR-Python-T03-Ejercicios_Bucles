#Escribe un programa que, dados dos números, uno real ( base ) y un entero positivo ( exponente ), saca por pantalla el resultado de la potencia.
#No se puede utilizar el operador de potencia.

print("introduce dos numeros")

num1=float(input("introduce base"))
num2=int(input("introduce un exponente"))

resultado=1
for n in range(num2):
    resultado= resultado * num1
print ("el resultado es:", resultado)