# Autor: Honorio
# Version: 1.0
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Para esto, se registran los días que trabajó y las horas de cada día.
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.
import os
os.system("cls")
N=int(input("Ingrese el número de trabajadores: "))
sueldo_horas=int(input("Ingrese el sueldo por hora: "))
for t in range (1,N+1):
    dia=int(input("Introduzca los dias que has trabajado: "))
    horas=int(input("Introduzca las horas trabajadas: "))

    total_horas = dia * horas
    sueldo = total_horas * sueldo_horas
print(f"Total pagado por la empresa a {N} empleados: {sueldo} €")
