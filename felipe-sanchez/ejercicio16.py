# Autor: Felipe
# Version: 1.0
# Ejercicio 16
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.


horas=float(input("Cuantras horas trabajaron los empleados esta semana: "))
precio=float(input("¿Cuanto cobran por hora?: "))
empleados=int(input("Dame el numero de trabajadores: "))

sueldo=horas*precio
total=sueldo*empleados


print("El sueldo de cada trabajador en esta semana es: ",sueldo)
print("La empresa paga un total de ", total, "€  por sus ",empleados,"empleados")