# Autor: Honorio
# Version: 1.0
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días)
#y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
import os
os.system("cls")

horas=0

for h in range(1,7):
    trabajo = int(input(f"Ingrese las horas trabajadas del día {h}: "))
    horas = trabajo + horas
sueldo_horas=float(input("Introduzca el sueldo de horas: "))

sueldo = horas * sueldo_horas
print(f"Total de horas trabajadas en la semana: {horas} horas")
print(f"Sueldo a recibir: ${sueldo}€")
