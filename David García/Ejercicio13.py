# Author: David García Pérez
# Version: 1.0

# Ejercicio 13
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días)
# y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

import os
os.system("cls")

print(" ")
print("#################### Calcular horas trabajadas ######################")
print(" ")

total_horas = 0

for dia in range(1, 7):
    horas = float(input(f"Introduce las horas trabajadas del día {dia}: "))
    total_horas = total_horas + horas

pago_por_hora = 10
sueldo = total_horas * pago_por_hora

print(f"Ha trabajado {total_horas} horas y ha recibido {sueldo} €")

print(" ")
print("#################### Fin del programa ######################")
print(" ")