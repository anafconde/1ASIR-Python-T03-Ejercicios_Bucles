# Autor: Paco Fernandez
# Version: 1.0
# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), 
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = float(input("Introduce un numero base: "))
exponente = int(input("Introduce un numero exponente: "))

resultado = 1

for p in range(exponente):
    resultado *= base  

print(f"{base} elevado a {exponente} es {resultado}")