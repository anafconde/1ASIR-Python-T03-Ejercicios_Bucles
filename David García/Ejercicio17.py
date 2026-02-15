# Author: David García Pérez
# Version: 1.0

# Ejercicio 17
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Para esto, se registran los días que trabajó y las horas de cada día.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

import os
os.system("cls")

print(" ")
print("#################### Calcular sueldos ######################")
print(" ")

num_trabajadores = int(input("Introduce el número de trabajadores: "))

total_empresa = 0
total_horas = 0

for t in range(1, num_trabajadores + 1):
    print(f"Trabajador {t}")
    
    dias = int(input("Introduce los días trabajados: "))
    pago_hora = int(input("Introduce el pago por hora: "))
    
    for d in range(1, dias + 1):
        horas = int(input(f"Horas trabajadas el día {d}: "))
        total_horas = total_horas + horas
    
    sueldo_semanal = total_horas * pago_hora
    total_empresa = total_empresa + sueldo_semanal
    
    print(f"Sueldo semanal del trabajador {t}: {sueldo_semanal} €")

print(f"Total pagado por la empresa a los {t} trabajadores: {total_empresa} €")

print(" ")
print("#################### Fin del programa ######################")
print(" ")